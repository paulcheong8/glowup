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
import axios from 'axios'


export default {
  name: "HomePage",
  components: {
    QuestionDialogue,
    Trending,
    AllPosts
  },
  data() {
    return {
    // trendingPosts: [
    //   {
    //     nickname: "hippo",
    //     organisation: "SMU",
    //     timePosted: "1d ago",
    //     category: "Technology",
    //     title: "Advice on career path",
    //     advice: "I am deciding whether to continue being a software engineer or going into something else..",
    //     numViews: 200,
    //     numComments: 20
    //   },
    //   {
    //     nickname: "monkey",
    //     organisation: "NUS",
    //     timePosted: "1w ago",
    //     category: "Career",
    //     title: "Is ABC Company good?",
    //     advice: "I got an offer from ABC but I am wondering if it is worth going there to start a career.",
    //     numViews: 256,
    //     numComments: 45
    //   },
    //   {
    //     nickname: "ducky",
    //     organisation: "NTU",
    //     timePosted: "3mth ago",
    //     category: "Career",
    //     title: "Tips on getting into X company",
    //     advice: "Anyone knows what kind of experience X company is looking for?",
    //     numViews: 456,
    //     numComments: 50
    //   },               
                      
    // ],
    posts: [],
    trendingPosts: [],
    // posts: [
    //   {
    //     nickname: "hippo",
    //     organisation: "SMU",
    //     timePosted: "1d ago",
    //     category: "Technology",
    //     title: "Advice on career path",
    //     advice: "I am deciding whether to continue being a software engineer or going into something else..",
    //     numViews: 200,
    //     numComments: 20,
    //     datetime: 1627199993684
    //   },
    //   {
    //     nickname: "monkey",
    //     organisation: "NUS",
    //     timePosted: "1w ago",
    //     category: "Career",
    //     title: "Is ABC Company good?",
    //     advice: "I got an offer from ABC but I am wondering if it is worth going there to start a career.",
    //     numViews: 100,
    //     numComments: 45,
    //     datetime: 1627200019390
    //   },
    //   {
    //     nickname: "ducky",
    //     organisation: "NTU",
    //     timePosted: "3mth ago",
    //     category: "Career",
    //     title: "Tips on getting into X company",
    //     advice: "Anyone knows what kind of experience X company is looking for?",
    //     numViews: 500,
    //     numComments: 50,
    //     datetime: 1627200215801
    //   },               
            
    //   {
    //     nickname: "monkey",
    //     organisation: "NUS",
    //     timePosted: "1w ago",
    //     category: "Career",
    //     title: "Is ABC Company good?",
    //     advice: "I got an offer from ABC but I am wondering if it is worth going there to start a career.",
    //     numViews: 256,
    //     numComments: 45,
    //     datetime: 1627200050089
    //   },
    //   {
    //     nickname: "ducky",
    //     organisation: "NTU",
    //     timePosted: "3mth ago",
    //     category: "Career",
    //     title: "Tips on getting into X company",
    //     advice: "heyoooo?",
    //     numViews: 456,
    //     numComments: 50,
    //     datetime: 1627200240296
    //   },                  
    // ],      
    updatedPosts: [],
    sort: "",
    }       

  },

  mounted: function() {
    // var StatsD = require('hot-shots');
    // var dogstatsd = new StatsD();

    // // Increment a counter.
    // dogstatsd.increment('page.views')    

    let config = {
      headers: {
        "Access-Control-Allow-Origin": "*",
        'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS'
      }
    }

    axios.get('http://ec2-3-237-88-193.compute-1.amazonaws.com:8000/getposts', config)
    .then(response => {
      for (let obj of response.data.posts) {
        this.posts.push(obj)
        if (this.trendingPosts.length < 3) {
          this.trendingPosts.push(obj)
        }
      }
    })
  }


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