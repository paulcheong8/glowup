<template>
  <v-container>
    <br><br><br><br><br><br>
    <h1>This is the {{this.searchKeyword}} page</h1>

  </v-container>

</template>

<script>

export default {
  name: 'search',
  data() {
    return {
      searchKeyword: "",
      adviceQuery: {
          nickname: "hippo",
          organisation: "SMU",
          timePosted: "1d ago",
          selectedCategories: ["Career", "Technology"],
          title: "Advice on career path",
          advice: "I am deciding whether to continue being a software engineer or going into something else..",
          numViews: 200,
          numComments: 20   
      },
      comments: [
        {
          nickname: "hippo",
          organisation: "SMU",
          timePosted: "1d ago",     
          numLikes: 12,
          numComments: 0      
        },
        {
          nickname: "hippo",
          organisation: "SMU",
          timePosted: "1d ago",     
          numLikes: 12,
          numComments: 0      
        }        
      ]
    }
  },
  async mounted() {
    try {
      this.searchKeyword = this.$route.query.searchKeyword
      console.log(this.searchKeyword)
    }
    catch (e) {console.log(e)}
  } 
}
</script>
