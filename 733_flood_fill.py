class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc] or len(image) == 0 or len(image[0]) == 0:
            return image
        
        image_pixel = image[sr][sc]
        image[sr][sc] = color

        if sr - 1 >= 0 and image[sr - 1][sc] == image_pixel:
            self.floodFill(image, sr - 1, sc, color)
        
        if sr + 1 < len(image) and image[sr + 1][sc] == image_pixel:
            self.floodFill(image, sr + 1, sc, color)
        
        if sc - 1 >= 0 and image[sr][sc - 1] == image_pixel:
            self.floodFill(image, sr, sc - 1, color)
        
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == image_pixel:
            self.floodFill(image, sr, sc + 1, color)

        return image
