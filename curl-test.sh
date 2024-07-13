#!/bin/bash

# Create a random post
RANDOM_NAME="TestUser$RANDOM"
RANDOM_EMAIL="test$RANDOM@example.com"
RANDOM_CONTENT="This is a test post with random content $RANDOM."

POST_RESPONSE=$(curl -s -X POST http://127.0.0.1:5000/api/timeline_post \
    -d "name=$RANDOM_NAME" \
    -d "email=$RANDOM_EMAIL" \
    -d "content=$RANDOM_CONTENT")

POST_ID=$(echo $POST_RESPONSE | jq -r '.id')

if [ "$POST_ID" == "null" ]; then
    echo "Failed to create post"
    exit 1
else
    echo "Post created successfully with ID: $POST_ID"
fi

# Retrieve all posts
GET_RESPONSE=$(curl -s http://127.0.0.1:5000/api/timeline_post)
echo "GET response: $GET_RESPONSE"

# Check if the created post is in the GET response
if echo "$GET_RESPONSE" | jq -e ".timeline_posts[] | select(.id == $POST_ID)" > /dev/null; then
    echo "Post is present in GET response"
else
    echo "Post is not present in GET response"
    exit 1
fi

# Clean up: delete the created post
DELETE_RESPONSE=$(curl -s -X DELETE http://127.0.0.1:5000/api/timeline_post/$POST_ID)
DELETE_MESSAGE=$(echo $DELETE_RESPONSE | jq -r '.message')

if [ "$DELETE_MESSAGE" == "Post deleted successfully" ]; then
    echo "Post deleted successfully"
else
    echo "Failed to delete post"
    exit 1
fi

echo "Test completed successfully"