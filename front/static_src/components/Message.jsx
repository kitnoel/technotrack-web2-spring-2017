import React from 'react';
import User from './User.jsx';
import connect from "react-redux/es/connect/connect";
import bindActionCreators from "redux/es/bindActionCreators";
// import {formatDate} from '../utils';


function formatDate(date) {
    return date.toLocaleDateString();
}

class MessageComponent extends React.Component {

    render() {
        return (
            <div className="Message">
                <User user={ this.props.author } />
                <div className="Message-content">
                    { this.props.content }
                </div>
                <div className="Message-date">
                    { this.props.created }
                </div>
            </div>
        );
    }
}


const mapStateToProps = (state, props) => {
    return {
        ...state.chats.messages[props.id],
        author: state.chats.users[state.chats.messages[props.id].author]
    };
};

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({}, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(MessageComponent);