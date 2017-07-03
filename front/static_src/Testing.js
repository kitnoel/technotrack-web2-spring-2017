export const POSTS = [
    {
        created: new Date(),
        content: 'I hope you enjoy learning React!',
        author: {
            username: 'Hello Kitty',
            avatarUrl: 'http://placekitten.com/g/64/64',
            id: 1,
        },
        id: 1
    },
    {
        created: new Date(),
        content: 'I hope you enjoy learning React!',
        author: {
            username: 'Goodbye Kitty',
            avatarUrl: 'http://placekitten.com/g/64/64',
            id: 2
        },
        id: 2
    },
    {
        created: new Date(),
        content: 'I hope you enjoy learning React!',
        author: {
            username: 'Hello Kitty',
            avatarUrl: 'http://placekitten.com/g/64/64',
            id: 3
        },
        id: 3
    }
];

export const CHATS = [
    {
        title: "Kittens",
        author: {
            username: 'Hello Kitty',
            avatarUrl: 'http://placekitten.com/g/64/64',
            id: 3
        },
        users: [
            {
                username: 'Hello Kitty',
                avatarUrl: 'http://placekitten.com/g/64/64',
                id: 3
            },
            {
                username: 'Goodbye Kitty',
                avatarUrl: 'http://placekitten.com/g/64/64',
                id: 2
            }
        ],
        messages: [
            {
                author: {
                    username: 'Goodbye Kitty',
                    avatarUrl: 'http://placekitten.com/g/64/64',
                    id: 2
                },
                content: "Lorem ipsum",
                created: new Date(),
                id: 1
            },
            {
                author: {
                    username: 'Goodbye Kitty',
                    avatarUrl: 'http://placekitten.com/g/64/64',
                    id: 2
                },
                content: "Lorem ipsum",
                created: new Date(),
                id: 2
            }
        ],
        last_message: {
            author: {
                username: 'Goodbye Kitty',
                avatarUrl: 'http://placekitten.com/g/64/64',
                id: 2
            },
            content: "Lorem ipsum",
            created: new Date(),
            id: 3
        },
        id: 1
    },
    {
        title: "Puppies",
        author: {
            username: 'Hello Kitty',
            avatarUrl: 'http://placekitten.com/g/64/64',
            id: 3
        },
        users: [
            {
                username: 'Hello Kitty',
                avatarUrl: 'http://placekitten.com/g/64/64',
                id: 3
            },
            {
                username: 'Goodbye Kitty',
                avatarUrl: 'http://placekitten.com/g/64/64',
                id: 2
            }
        ],
        messages: [
            {
                author: {
                    username: 'Goodbye Kitty',
                    avatarUrl: 'http://placekitten.com/g/64/64',
                    id: 2
                },
                content: "Lorem ipsum",
                created: new Date(),
                id: 3
            },
            {
                author: {
                    username: 'Goodbye Kitty',
                    avatarUrl: 'http://placekitten.com/g/64/64',
                    id: 2
                },
                content: "Lorem ipsum",
                created: new Date(),
                id: 4
            }
        ],
        last_message: {
            author: {
                username: 'Goodbye Kitty',
                avatarUrl: 'http://placekitten.com/g/64/64',
                id: 2
            },
            content: "Lorem ipsum",
            created: new Date(),
            id: 3
        },
        id: 2
    }
];