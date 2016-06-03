class Connection {
    constructor(url) {
        this._url = url;
        this._socket = null;
        this._handlers = {};
        this._messages = [];
        this._id = 0;
        this._reconnectAttempts = 0;
        this._reconnectAttemptsMax = 5;
        this._connect();
    }

    _onopen(event) {
        console.log('Connection established');
        this.onopen && this.onopen(event);
    }

    _onclose(event) {
        console.log('Connection closed');
        this._socket = null;
        this.onerror && this.onerror(event);
        this._reconnect();
    }

    _onmessage(event) {
        const {request_id, name, body} = JSON.parse(event.data);
        const handler = this._handlers[request_id];
        handler && delete this._handlers[request_id];
        handler && handler.resolve(body);
    }

    _connect() {
        console.log('Connecting...');
        this._socket = new WebSocket(this._url);
        this._socket.onopen = this._onopen.bind(this);
        this._socket.onclose = this._onclose.bind(this);
        this._socket.onmessage = this._onmessage.bind(this);
    }

    _reconnect() {
        if (this._reconnectAttempts < this._reconnectAttemptsMax) {
            const delay = 1000 * Math.pow(2, this._reconnectAttempts++);
            setTimeout(this._connect.bind(this), delay);
            console.log('Reconnecting in', delay, 'seconds');
        }
        else {
            console.log('Exceeded max reconnect attempts, should reload page');
        }
    }

    _send(message) {
        try {
            this._socket.send(JSON.stringify(message))
        }
        catch (exc) {
            this._messages.push(message);
        }
    }

    call(endpoint, payload) {
        const id = this._id++;
        const message = {
            name: 'request',
            request_id: id.toString(),
            handler: endpoint,
            body: payload
        };
        return new Promise((resolve, reject) => {
            this._handlers[id] = {resolve, reject};
            this._send(message);
        });
    }

    subscribe(endpoint, handler) {
        throw Error('Not implemented method');
    }
}



export default function configureConnection(url) {
    return new Connection(url);
};