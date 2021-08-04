<template>
    <v-card elevation='0'>
      <v-card-text class="my-5 text-left">
        <p class="" style="font-size:2em;">
          All posts
        </p>      
      </v-card-text>
      
      <v-row>
      <v-col cols="3">

        <p align="left" class="mx-3" style="font-size:0.9em;">
          Filter by
        </p>        
        <v-combobox
          v-model="categorySelect"
          :items="categoryItems"
          outlined
          multiple
          clearable
          small-chips
          label="Category"
          @change="categoryClicked" 
        ></v-combobox>

        <p align="left" class="mx-3" style="font-size:0.9em;">
          Sort by
        </p>        
        <v-row align="center" >   

          <v-btn-toggle
            v-model="sort"
            dense
            outlined      
            color="orange"
            class="ma-3"
            mandatory
          >
            <v-btn
              value="popular"
              @click="sortBy"
            >
              Popular
            </v-btn>

            <v-btn
              value="latest"
              @click="sortBy"
            >
              Latest
            </v-btn>        

          </v-btn-toggle>          
        </v-row>
      
      </v-col>
      <v-col cols="8">
        <v-row
          v-for="(post, i) in updatedPosts"
          :key=i
          justify="center"
          class="my-3"
        >
            <v-card
              class="text-left"
              width="800"
              outlined
              @click="postSearch(post)"
              :ripple="false"            
            >
              <v-row class="">
                <v-card-text>
                  <v-chip-group
                  >
                    <v-chip 
                      small                
                      :class="`${post.selectedCategory} ma-2`"     
                      @click="categorySearch(post.selectedCategory)"      
                    >
                      {{post.selectedCategory}}
                    </v-chip>
                  </v-chip-group>
                </v-card-text>
              </v-row>

              <span class="mx-4 subheading" style="font-size:14px">{{post.nickname}} | {{post.organisation}}</span>

              <v-card-title class="text--primary">
                  {{post.advice | limitString(150)}}
              </v-card-title>

              <v-card-text>
                {{post.advice | limitString(200)}}
              </v-card-text>

              <v-card-actions>
                  <v-list-item class="">

                  <v-list-item-content>
                      <v-list-item-subtitle>{{post.timePosted}}</v-list-item-subtitle>
                  </v-list-item-content>
              
                  <v-row
                      align="center"
                      justify="end"
                  >             
                      <v-icon small class="subheading mr-3">
                        mdi-eye
                      </v-icon>

                    <span class="subheading mr-3" style="font-size:13px">{{post.numViews}}</span>
                    
                    <span class="mr-1">·</span>

                    <v-btn
                      icon
                    >               
                      <v-icon small>
                      mdi-comment
                      </v-icon>
                    </v-btn>

                      <span class="subheading" style="font-size:13px">{{post.numComments}}</span>
                  </v-row>
                  </v-list-item>
              </v-card-actions>
            </v-card>
          
        </v-row>           
      </v-col>
      </v-row>

 
    </v-card>
</template>

<script>
export default {
  props: ['udpatedPosts', 'posts'],
  data: () => ({
    sort: "",
    updatedPosts: [],
    categorySelect: [],
    categoryItems: ['Technology', 'Finance', 'Internship', 'Graduate Program', 'Traineeship', 'Career', 'Misc'],

  })
  ,
    async mounted() {
      this.updatedPosts = this.posts
      this.sortBy()
      let date = ""
      date = new Date().getTime()
      console.log(date)
    },  
  methods: {
      postSearch: function(post) {
        this.$router.push({ path: "/post", query: {post: post}})
      },
      categorySearch: function(category) {
        this.$router.push({ path: "/search", query: {searchKeyword: category} })
      },        
      categoryClicked: function() {
        this.filterCategory();
      },

      filterCategory: function() {
        var parsedobj = JSON.parse(JSON.stringify(this.categorySelect))
        if (parsedobj.length === 0) {
          this.updatedPosts = this.posts
        }
        else {
          this.updatedPosts = []
          this.posts.forEach(post => {
            if (parsedobj.includes(post.selectedCategory)) {
                this.updatedPosts.push(post)
            }
          })     
        }
      },

      sortBy: function() {
        if (this.sort == "popular") {
          this.updatedPosts.sort((a, b) => b.datetime.toString().localeCompare(a.datetime))
        } else {
          this.updatedPosts.sort((a, b) => b.numViews.toString().localeCompare(a.numViews))
        }
      },      
  },
    filters: {

        limitString: function(value, size) {
        if (!value) return ''
        value = value.toString()
        if (value.length <= size) {
            return value;
        }
        return value.substr(0,size) + '...';
        }
    }    
      
}
</script>