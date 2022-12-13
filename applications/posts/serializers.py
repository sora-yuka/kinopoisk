from rest_framework import serializers

from applications.posts.models import Category, Comment, Image, Like, Post, Rating

from django.db.models import Avg
        
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
  
        
class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = '__all__'
        

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only = True)
    images = ImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'
        
    def create(self, validated_data):
        request = self.context.get('request')
        files_data = request.FILES
        
        # TODO: save pictures and in admin show likes for each picture
        post = Post.objects.create(**validated_data)
        
        # print(images_data)
        for image in files_data.getlist('images'):
            print(image)
            Image.objects.create(post=post, image=image)  
        return post
    
        
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = instance.likes.filter(like=True).count()
        rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        return rep
        
    
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        print(instance)
        if not instance.parent:
            rep.pop('parent')
        return rep
        
        
class RatingSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField()
    rating = serializers.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Rating
        fields = ['rating']
        
        
        
        
        
        
    
        
        
    
        
        