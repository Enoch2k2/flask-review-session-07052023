# Flask Review Session 07052023

For this challenge, you will pair with another student.

This challenge you will:
* associate the users, blogs, and comments
* a user will has many comments
* a user will has many blogs through comments
* a comment will belong to a user
* a comment will belong to a blogs
* a blog will has many comments
* a blog will has many users through comments

Once correctly associated, create seed data in the seeds.py.

Once the database has been seeded, go into the app.py and update the get route to return the json in this format:

```
{
    blogs: [
        {
            id: 1,
            title: "Blog title 1",
            content: "Blog content 1",
            "comments": [
                {
                    id: 1,
                    "content: "Comment content 1",
                    "user": {
                        id: 1,
                        username: "Sam"
                    }
                },
                {
                    id: 2,
                    "content: "Comment content 2",
                    "user": {
                        id: 2,
                        username: "Bob"
                    }
                }
            ]
        },
        {
            id: 2,
            title: "Blog title 2",
            content: "Blog content 2",
            "comments": [
                {
                    id: 3,
                    "content: "Comment content 3",
                    "user": {
                        id: 2,
                        username: "Bob"
                    }
                }
            ]
        },
    ]
}
```