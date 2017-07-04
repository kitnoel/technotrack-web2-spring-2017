import fetch from 'isomorphic-fetch';
import FormData from 'form-data';
import Cookies from 'js-cookie';

export const SEND_POST = 'SEND_POST';
export const LOAD_POSTS = 'LOAD_POSTS';
export const LOAD_POSTS_SUCCESS = 'LOAD_POSTS_SUCCESS';
export const LOAD_POSTS_ERROR = 'LOAD_POSTS_ERROR';
export const SEARCH_POSTS = 'SEARCH_POSTS';
export const SEARCH_POSTS_SUCCESS = 'SEARCH_POSTS_SUCCESS';

export function addPost(post) {
    return {
        type: ADD_POST,
        post
    };
}

export function loadPosts() {
    return {
        type: LOAD_POSTS,
    };
}

export function loadPostsSuccess(responce) {
    return {
        type: LOAD_POSTS_SUCCESS,
        responce
    };
}

export function searchPosts() {
    return {
        type: SEARCH_POSTS,
    };
}

export function searchPostsSuccess(responce) {
    return {
        type: SEARCH_POSTS_SUCCESS,
        responce
    };
}


export function loadPostsError() {
    return {
        type: LOAD_POSTS_ERROR,
    };
}

export function fetchPosts() {
    return dispatch => {
        dispatch(loadPosts());
        return fetch('/api/posts/', {
            credentials: "same-origin",
        })
            .then(responce => responce.json())
            .then(json => {console.log(json); return json;})
            .then(json => dispatch(loadPostsSuccess(json)));
    };
}

export function fetchSearchPosts(text) {
    return dispatch => {
        dispatch(searchPosts());
        // let formData = new FormData();
        // formData.append('csrfmiddlewaretoken', Cookies.get('csrftoken'));
        return fetch('/api/posts/search/?content__contains='+text, {
            credentials: "same-origin",
        })
            .then(responce => responce.json())
            .then(json => {console.log(json); return json;})
            .then(json => dispatch(searchPostsSuccess(json)));
    };
}

export function sendPost(post) {
    return dispatch => {
        let formData = new FormData();
        formData.append('content', post.content);
        formData.append('csrfmiddlewaretoken', Cookies.get('csrftoken'));
        return fetch('/api/posts/', {
            credentials: "same-origin",
            method: 'POST',
            body: formData
        })
            .then(responce => {console.log(responce.body)})
            .then(() => dispatch(fetchPosts()));

    };
}

export function deletePost(postId) {
    return dispatch => {
        return fetch('/api/posts/' + postId, {
            credentials: "same-origin",
            method: 'DELETE',
            headers: {
                'X-CSRFTOKEN': Cookies.get('csrftoken')
            }
        })
            .then(responce => {console.log(responce)})
            .then(() => dispatch(fetchPosts()));

    };
}