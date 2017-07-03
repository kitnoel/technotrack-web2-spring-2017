import React from 'react';
import User from './User.jsx';
// import {formatDate} from '../utils';

import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import Button from "react-bootstrap/es/Button";
import Glyphicon from "react-bootstrap/es/Glyphicon";
import {deletePost} from "../actions/posts.jsx";


function formatDate(date) {
    return date.toLocaleDateString();
}

class PostComponent extends React.Component {

    deletePost = () => {
        this.props.deletePost(this.props.id);
    };

    render() {
        return (
            <div className="Post">
                <User user={ this.props.author } />
                <div className="Post-content">
                    { this.props.content }
                </div>
                <div className="Post-date">
                    { this.props.created }
                </div>
                <Button onClick={ this.deletePost } ><Glyphicon glyph="remove" /></Button>
            </div>
        );
    }
}

const mapStateToProps = (state, props) => ({
    ...state.posts.posts[props.id],
    author: state.posts.users[state.posts.posts[props.id].author]
});

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({
        deletePost
    }, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(PostComponent);

// export default PostComponent;
