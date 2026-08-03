class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        self.tweets[userId].append((self.counter, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        for tweet in self.tweets[userId]:
            heapq.heappush(heap, tweet)

            if len(heap) > 10:
                heapq.heappop(heap)

        for user in self.follow_map[userId]:
            for tweet in self.tweets[user]:
                heapq.heappush(heap, tweet)

                if len(heap) > 10:
                    heapq.heappop(heap)

        return [tweet[1] for tweet in sorted(heap, reverse=True)]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        self.follow_map[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_map[followerId]:
            return

        self.follow_map[followerId].remove(followeeId)
        
