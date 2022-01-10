<template>
  <v-container class="my-15">

      <!-- post section -->
      <v-row justify="center">
          <v-card
            class="mx-2 my-5 text-left"
            max-width="600"
          >
            <v-row class="">
            <v-card-subtitle     
                >
                <div>
                <v-chip 
                    small
                    :class="`${post.category} ma-2`"     
                    @click="categorySearch(post.category)"      
                >
                    {{post.category}}
                </v-chip>
                </div>
            </v-card-subtitle>
            </v-row>

            <v-card-title>
                {{post.title}}        
            </v-card-title>

            <v-card-subtitle >
                {{post.nickname}} | {{post.organisation}}
            </v-card-subtitle>   

            <v-card-text class="text--primary">
                {{post.advice}}
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
                    <v-icon small class="mr-1">
                    mdi-eye
                    </v-icon>
                    <span class="subheading mr-2" style="font-size:13px">{{post.numViews}}</span>
                    
                    <span class="mr-1">·</span>
                    <v-icon small class="mr-1">
                    mdi-comment
                    </v-icon>
                    <span class="subheading" style="font-size:13px">{{post.numComments}}</span>
                </v-row>
                </v-list-item>
            </v-card-actions>

            <v-divider></v-divider>

            <v-container>

                <v-text-field
                  v-model= "nickname"
                  label="Nickname"
                  required
                  color="amber darken-1"
                ></v-text-field>

                <v-textarea
                    v-model= "comment"
                    name="input-7-1-4"
                    color="amber darken-1"
                    label="What do you think?"
                    auto-grow
                >
                </v-textarea>        
                
                <v-row class="my-1 mr-1" justify="end">
                <v-btn 
                    small
                    @click=addComment
                    color="amber darken-1"
                    justify="end"
                >
                    Add comment
                </v-btn>              
                </v-row>                
            </v-container>    


          </v-card>

          
      </v-row>
      
      <!-- comments -->
      <v-row
        v-for="(c, i) in comments"
        :key=i
        justify="center"
        class="my-3"
      >
          <v-card
            class="mx-2 my-2 text-left"
            width="600"
            
          >

            <v-card-subtitle >
                {{c.nickname}} | {{c.organisation}}
            </v-card-subtitle>   

            <v-card-text class="text--primary">
                {{c.comment}}
            </v-card-text>

            <v-card-actions>
                <v-list-item class="">

                <v-list-item-content>
                    <v-list-item-subtitle>{{c.timePosted}}</v-list-item-subtitle>
                </v-list-item-content>
            
                <v-row
                    align="center"
                    justify="end"
                >
                  <v-btn
                    icon
                    :color="c.liked === true ? 'amber darken-1' : 'grey darken-1'"
                    @click="likeComment(c)"
                  >                
                    <v-icon small>
                      mdi-thumb-up
                    </v-icon>
                  </v-btn>

                  <span class="subheading mr-3" style="font-size:13px">{{c.numLikes}}</span>
                  
                  <span class="mr-1">·</span>

                  <v-btn
                    icon
                  >               
                    <v-icon small>
                    mdi-comment
                    </v-icon>
                  </v-btn>

                    <span class="subheading" style="font-size:13px">{{c.numComments}}</span>
                </v-row>
                </v-list-item>
            </v-card-actions>
          </v-card>
        
      </v-row>

  </v-container>

</template>

<script>
import axios from 'axios'

export default {
  name: 'search',
  data() {
    return {
      post: {},
      nickname: "",
      comment: "",
      // liked: false,
      formRules: [
        v => !!v || 'This field is required',
      ],      
      comments: [],
      // comments: [
      //   {
      //     nickname: "bunny",
      //     comment: "I feel that maybe you should look into what are your interests. See what aligns with it and move into that area",
      //     organisation: "SMU",
      //     timePosted: "1d ago",     
      //     numLikes: 12,
      //     numComments: 0,
      //     // liked: false
      //   },
      //   {
      //     nickname: "moosey",
      //     comment: "Think about what you like and whether you can see yourself doing it for the next few years. Remember not to choose based on salary as well.",
      //     organisation: "SMU",
      //     timePosted: "1d ago",     
      //     numLikes: 15,
      //     numComments: 0,
      //     // liked: false      
      //   }        
      // ]
    }
  },
  methods: {
      categorySearch: function(category) {
        this.$router.push({ path: "/search", query: {searchKeyword: category} })
      },      
      addComment: function() {
        let commentObj = {}
        console.log(this.comment)
        commentObj = {
          post_id: this.post.post_id,
          nickname: this.nickname,
          comment: this.comment,
          // organisation: "NTU",
        //  timePosted: "1d ago",
          // numLikes: 0,
          // numComments: 0,
        }
        axios.post('http://ec2-3-237-88-193.compute-1.amazonaws.com/createcomment/', commentObj)
        this.comments.push(commentObj)
        console.log(commentObj)
      },

      likeComment: function(c) {
        if (!c.liked) {
          c.numLikes += 1
          // let likeObj = {
          //   comment_id: c.comment_id,
          //   user_id: 1
          // }
          // axios.post('http://localhost:80/createlike/', likeObj)
        } else {
          c.numLikes -= 1
        }
          
        c.liked = !c.liked
        console.log(c.liked) 
      }
  },
  async mounted() {
    try {
        this.post = this.$route.query.post
        axios.get('http://ec2-3-237-88-193.compute-1.amazonaws.com/getcomments', {
          params: {
            post_id: this.post.post_id
          }
        }).then(response => {
          for (let obj of response.data.comments) {
            this.comments.push(obj)
          }
        })
        console.log(this.comments)
    }
    catch (e) {console.log(e)}
  } 
}
</script>
