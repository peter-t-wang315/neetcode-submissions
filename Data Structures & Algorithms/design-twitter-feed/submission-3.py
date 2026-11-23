import heapq
class Twitter:
    def __init__(self):
        self.userFollowing = {}
        self.userPosts = {}
        self.currPostI = 1000

    def postTweet(self, userId: int, tweetId: int) -> None:
        # If new user, create new userId and set in userFollowing and userPosts
        if userId not in self.userFollowing:
            self.userFollowing[userId] = {userId}
            self.userPosts[userId] = []
        
        # Add post to userPosts with (currPostI, userId, tweetId)
        self.userPosts[userId].append((self.currPostI, userId, tweetId, len(self.userPosts[userId])))
        # decrement currPostI
        self.currPostI -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if len(self.userFollowing) == 0:
            return []

        # Create new heap and output
        heap = []
        output = []
        # Iterate over all following
        for following in self.userFollowing[userId]:
            # Append each latest post to heap
            heapq.heappush(heap, self.userPosts[following][-1])

        # Iterate until at 10 posts or heap is empty
        while len(output) < 10 and len(heap) > 0:
            # pop heap item and add to output
            tweet = heapq.heappop(heap)
            output.append(tweet[2])
            # find user popped from, then append next latest post from user to heap
            if tweet[3] > 0:
                heapq.heappush(heap, self.userPosts[tweet[1]][tweet[3]-1])
        
        # Return output
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.userFollowing:
            self.userFollowing[followerId] = set()

        # Add to userFollowing
        self.userFollowing[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        # remove from userFollowing set
        self.userFollowing[followerId].discard(followeeId)
        
