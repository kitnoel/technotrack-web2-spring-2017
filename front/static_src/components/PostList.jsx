import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import Post from './Post.jsx';
import ListGroup from "react-bootstrap/es/ListGroup";
import ListGroupItem from "react-bootstrap/es/ListGroupItem";
import FormGroup from "react-bootstrap/es/FormGroup";
import Button from "react-bootstrap/es/Button";
import ControlLabel from "react-bootstrap/es/ControlLabel";
import FormControl from "react-bootstrap/es/FormControl";
import Col from "react-bootstrap/es/Col";
import { fetchPosts, sendPost } from "../actions/posts.jsx";
import Row from "react-bootstrap/es/Row";

class PostListComponent extends React.Component {

    state = {
        formContent: ''
    };

    handleChange = (e) => {
        this.setState({ formContent: e.target.value });
    };

    componentDidMount() {
        this.props.fetchPosts()
    };

    sendPost = () => {
        this.props.sendPost({
            content: this.state.formContent
        });
        this.setState({ formContent: '' });
    };

    render() {
        const list = this.props.postList.map(
            id => <ListGroupItem key={ id }>
                <Post
                    id={ id }
                />
            </ListGroupItem>
        );
        return (
            <div>
                <Col xs={12} md={8}>
                    <FormGroup>
                        <ControlLabel>Feed</ControlLabel>
                    </FormGroup>

                    <FormGroup controlId="formControlsTextarea">
                        <ControlLabel>Add your post:</ControlLabel>
                        <FormControl componentClass="textarea" placeholder="textarea" onChange={this.handleChange}/>
                    </FormGroup>


                    <Button type="submit" onClick={ this.sendPost }>
                        Submit
                    </Button>
                    { this.props.isLoading ? <div>Loading...</div> : <div></div> }
                    <ListGroup>
                        { list }
                    </ListGroup>
                </Col>
            </div>
        );
    }
}

const mapStateToProps = state => ({
    postList: state.posts.postList,
    isLoading: state.posts.isLoading
});

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({
        fetchPosts,
        sendPost
    }, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(PostListComponent);
