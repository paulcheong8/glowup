<template>
  <v-container class="my-16">

    <!-- question dialogue form -->
    <QuestionDialogue
      v-bind:posts="this.posts"
    />

    <!-- trending section  -->
    <Trending
      v-bind:trendingPosts="this.trendingPosts"
    />

    <!-- all posts section -->
    <AllPosts
      v-bind:updatedPosts="this.updatedPosts"
      v-bind:posts="this.posts"
    />

  </v-container>
</template>

<script>
import QuestionDialogue from '../components/QuestionDialogue.vue'
import Trending from '../components/Trending.vue'
import AllPosts from '../components/AllPosts.vue'

  export default {
    name: "HomePage",
    components: {
      QuestionDialogue,
      Trending,
      AllPosts
    },
    data: () => ({       
      trendingPosts: [
        {
          nickname: "hippo",
          organisation: "SMU",
          timePosted: "1d ago",
          selectedCategory: "Technology",
          title: "Advice on career path",
          advice: "I am deciding whether to continue being a software engineer or going into something else..",
          numViews: 200,
          numComments: 20
        },
        {
          nickname: "monkey",
          organisation: "NUS",
          timePosted: "1w ago",
          selectedCategory: "Career",
          title: "Is ABC Company good?",
          advice: "I got an offer from ABC but I am wondering if it is worth going there to start a career.",
          numViews: 256,
          numComments: 45
        },
        {
          nickname: "ducky",
          organisation: "NTU",
          timePosted: "3mth ago",
          selectedCategory: "Career",
          title: "Tips on getting into X company",
          advice: "Anyone knows what kind of experience X company is looking for?",
          numViews: 456,
          numComments: 50
        },               
                        
      ],
      posts: [
        {
          nickname: "hippo",
          organisation: "SMU",
          timePosted: "1d ago",
          selectedCategory: "Technology",
          title: "Advice on career path",
          advice: "I am deciding whether to continue being a software engineer or going into something else..",
          numViews: 200,
          numComments: 20,
          datetime: 1627199993684
        },
        {
          nickname: "monkey",
          organisation: "NUS",
          timePosted: "1w ago",
          selectedCategory: "Career",
          title: "Is ABC Company good?",
          advice: "I got an offer from ABC but I am wondering if it is worth going there to start a career.",
          numViews: 100,
          numComments: 45,
          datetime: 1627200019390
        },
        {
          nickname: "ducky",
          organisation: "NTU",
          timePosted: "3mth ago",
          selectedCategory: "Career",
          title: "Tips on getting into X company",
          advice: "Anyone knows what kind of experience X company is looking for?",
          numViews: 500,
          numComments: 50,
          datetime: 1627200215801
        },               
              
        {
          nickname: "monkey",
          organisation: "NUS",
          timePosted: "1w ago",
          selectedCategory: "Career",
          title: "Is ABC Company good?",
          advice: "I got an offer from ABC but I am wondering if it is worth going there to start a career.",
          numViews: 256,
          numComments: 45,
          datetime: 1627200050089
        },
        {
          nickname: "ducky",
          organisation: "NTU",
          timePosted: "3mth ago",
          selectedCategory: "Career",
          title: "Tips on getting into X company",
          advice: "heyoooo?",
          numViews: 456,
          numComments: 50,
          datetime: 1627200240296
        },                  
      ],      
      updatedPosts: [],
      sort: "",
    }),

    methods: {
 
    },
  

  }
</script>

<style>

.v-chip.Career {
 background: orange;  
}

.v-chip.Technology {
 background: blue;  
}

</style>