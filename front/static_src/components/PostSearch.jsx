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
import {fetchSearchPosts, searchPosts} from "../actions/posts.jsx";

class PostSearchComponent extends React.Component {

    state = {
        formContent: ''
    };

    handleChange = (e) => {
        this.setState({ formContent: e.target.value });
    };

    componentDidMount() {
    };

    searchPosts = () => {
        this.props.fetchSearchPosts(this.state.formContent);
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
                        <ControlLabel>Insert search text</ControlLabel>
                        <FormControl componentClass="textarea" placeholder="textarea" onChange={this.handleChange}/>
                    </FormGroup>


                    <Button type="submit" onClick={ this.searchPosts }>
                        Search
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
    postList: state.posts.searchPostList,
    isLoading: state.posts.searching
});

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({
        fetchSearchPosts
    }, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(PostSearchComponent);
