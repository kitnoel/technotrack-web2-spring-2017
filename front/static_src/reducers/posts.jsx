import {
    SEND_POST,
    LOAD_POSTS,
    LOAD_POSTS_SUCCESS,
    LOAD_POSTS_ERROR,
    SEARCH_POSTS,
    SEARCH_POSTS_SUCCESS
} from '../actions/posts.jsx';
import update from 'react-addons-update';


const initialStore = {
    postList: [],
    posts: {},
    users: {},
    isLoading: false,
    searchPostList: [],
    searching: false
};

export default function posts(store = initialStore, action) {
    switch (action.type) {
    case LOAD_POSTS:
        return update(store, {
            isLoading: { $set: true }
        });
    case LOAD_POSTS_SUCCESS:
        return update(store, {
            isLoading: { $set: false },
            postList: { $set: action.normResponce.result },
            posts: { $merge: action.normResponce.entities.posts },
            users: { $merge: action.normResponce.entities.users }
        });
    case LOAD_POSTS_ERROR:
        return update(store, {
            isLoading: { $set: false }
        });
    case SEARCH_POSTS:
        return update(store, {
            searching: { $set: true }
        });
    case SEARCH_POSTS_SUCCESS:
        console.log(action.responce);
        console.log(action.normResponce);
        return update(store, {
            searching: { $set: false },
            searchPostList: { $set: action.normResponce.result },
            posts: { $merge: action.normResponce.entities.posts },
            users: { $merge: action.normResponce.entities.users }
        });
    default:
        return store;
    }
}
