const initialState = {
    isLoading: true,
    title: null,
    stream: null,
    items: [],
    filters: {},
    errors: {},
    total: 0,
    pageSize: 20,
    page: 1,
    order: '+id'
};


export default function stream(state=initialState, action={}) {
    if (action.type === 'STREAM_UPDATE_REQUEST') {
        return {
            ...initialState,
            isLoading: true
        };
    }

    if (action.type === 'STREAM_UPDATE_SUCCESS') {
        return {
            ...state,
            isLoading: false,
            title: action.payload.title,
            stream: action.payload.stream,
            items: action.payload.items,
            filters: action.payload.filters,
            errors: action.payload.errors,
            total: action.payload.total,
            pageSize: action.payload.page_size,
            page: action.payload.page
        };
    }

    if (action.type === 'STREAM_UPDATE_FAILURE') {
        return {
            ...initialState,
            isLoading: false
        };
    }

    return state;
}