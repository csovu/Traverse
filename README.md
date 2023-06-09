# Traverse

http://csovu.pythonanywhere.com

## Overview
    TripReport is a blog-social media site allowing users to upload their trip information. Details include location, distances(milage), maps, images, planning considerations an overall description of how the trip went, and future considerations. While this is primarily a platform for new routes through the backcountry, popular existing trails (PCT,AT,CDT, etc.) are welcome, too. 

## Features
    #### User Stories
        - As a backpacker, I want to visit a new area but don't know where to go.
        - As an outdoors-person I want to share a cool trip I went on in detail, but I don't want run my own website to do it. 
    #### Tasks
        - Users have unique profiles
        - Users can make a post to include text and images
        - Users can browse posts from other site users
## Data Models
    ####Models
        - CustomUser(signup)
            -about (CharFeild=1000)
            -location (CharFeild, null=True, blank=True)
            -saved posts (null=True, blank=True)

        - Posts
            -TripTitle - models.CharField(max_length=50, blank=False) 
            -TripSummery = models.CharField(max_length=2000, blank=False) (does this need multipe text fields for various inputs? general discription, planning, considerations?)
            -TrailConditions = models.CharField(max_length=2000, null=True, blank=True)
            -PlanningInfo = models.CharField(max_length=2000, null=True, blank=True)
            -OtherDetails = models.CharField(max_length=2000, null=True, blank=True)
            -date-posted = models.DateField(default=date.today)
            -last-edited = models.DateTimeField(null=True, auto_now=True)
            -location(user input text or geocoding API) 
            -mapDetails = models.URLField(max_length=300, null=True, blank=True) (for attaching url to map files from other sites)
            -user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

        -PostImages
            -multiple images that go with a post (Forign Key)

        - (View)Search
            - generalized search box that searches text in a post, user name or location

        - vote object- who, what, score up/down vote(two foeriegn key relationship), a vote set on the object 
## Shedule
    #### Week 1 
        - Day 1: set up user login and models
        - Day 2-3: URLS for main page, individual user posts, user profile page
        - Day 3: user can post text and see other users
        - Day 4-5: HTML/CSS
    #### Week 2
        -Day 1-2: user can edit their own 'About Me' page and edit posts
        -Day 2-5: user can upload images
    #### Week 3
        - Day 1-3:Users can like Posts
        - Day 4-5: HTML/CSS refinement 
    #### Week 4
        - Day 1: Search ablility
        - Day 2-3: Users can save Posts
        - Day 3-4: Posts can be filtered by most popular
        - Day 5: HTML/CSS final touches
    #### Nice-to-have
        - nested posts/user can orgnize their own posts into files 
        - comments on posts (moderation is a concern, therefor this is not part of the MVP)
        - users can add eachother as friends
        - user messaging (DM)

Future problems= how to enforce one required image per post 
