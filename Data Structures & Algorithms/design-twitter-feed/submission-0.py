class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        self.tweets[userId].append((self.counter, tweetId))
        


    def getNewsFeed(self, userId: int) -> List[int]:
        heap = [(tweet[0], tweet[1]) for tweet in self.tweets[userId]]
        heapq.heapify(heap)

        while len(heap) > 10:
            heapq.heappop(heap)

        followees = self.follows[userId]

        for followee in followees:
            for tweet in self.tweets[followee]:
                heapq.heappush(heap, (tweet[0], tweet[1]))

                if len(heap) > 10:
                    heapq.heappop(heap)

        return [tweet[1] for tweet in sorted(heap, reverse=True)]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        self.follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follows[followerId]:
            return 

        self.follows[followerId].remove(followeeId)
        
