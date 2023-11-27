import pytest


@pytest.mark.parametrize("input_user_id, output_user_id",
                         [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])
def test_users(api_client, input_user_id, output_user_id):
    response = api_client.get(path=f"/users",
                              params={
                                  "id": input_user_id}
                              ).json()
    assert response[0]["id"] == output_user_id


@pytest.mark.parametrize("input_post_id_comment, output_post_id_comment",
                         [(1, 1),
                          (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)
                          ])
def test_comments(api_client, input_post_id_comment, output_post_id_comment):
    response = api_client.get(path=f"/posts/{input_post_id_comment}/comments",
                              params={
                                  "postId": input_post_id_comment}
                              ).json()
    print(f"Post ID: {input_post_id_comment} have {len(response)} comments")
    for item in response:
        assert item["postId"] == output_post_id_comment