import React from 'react';

class Avatar extends React.Component {
    render() {
        return (
            <img className="Avatar"
             // src={this.props.user.avatarUrl}
             src={"http://placekitten.com/g/64/64"}
             alt={this.props.user.username}
            />
        );
    }
}
class UserComponent extends React.Component {

    render() {
        return (
            <div className="UserInfo">
                <Avatar user={this.props.user}/>
                <div className="UserInfo-name">
                    <strong>{this.props.user.username}</strong>
                </div>
            </div>

        );
    }
}

export default UserComponent;
