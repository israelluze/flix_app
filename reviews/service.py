from reviews.repository import ReviewRepository

class ReviewService:

    def __init__(self):
        self.review_repository = ReviewRepository()

    def get_reviews(self):
        return self.review_repository.get_reviews()
    
    def create_review(self, stars, comment, movie):
        review = dict(
            stars=stars,
            comment=comment,
            movie=movie
        )
        return self.review_repository.create_review(review)