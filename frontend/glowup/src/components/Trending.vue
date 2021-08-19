<template>
    <v-card elevation="0" height="400">

        <v-card-text class="my-5 text-left">
        <p class="" style="font-size:2em;">
            Trending
        </p>      
        </v-card-text>

        <v-row justify="center">
        <v-card
            v-for="(post,i) in trendingPosts"
            :key=i
            @click="postSearch(post)"
            :ripple="false"
            class="mx-2 my-2 text-left"
            width="300" 
            max-height="325"
        >
            <v-row class="">
            <v-card-text>
                <v-chip-group
                
                >
                <v-chip 
                    small
                    :class="`${post.category} ma-2`"     
                    @click="categorySearch(post.category)"      
                >
                    {{post.category}}
                </v-chip>
                </v-chip-group>
            </v-card-text>
            </v-row>

            <v-card-title>
                {{post.title | limitString(45)}}        
            </v-card-title>

            <v-card-subtitle >
            {{post.nickname}} | {{post.organisation}}
            </v-card-subtitle>   

            <v-card-text class="text--primary">
            {{post.advice | limitString(100)}}
            </v-card-text>

            <!-- date, views, comments -->
            <v-card-actions>
            <v-list-item class="">
                <!-- <v-list-item-avatar color="grey darken-3">
                <v-img
                    class="elevation-6"
                    alt=""
                    src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
                ></v-img>
                </v-list-item-avatar> -->

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




        </v-card>  
        </v-row>
    </v-card> 
</template>

<script>
export default {
  props: ['trendingPosts'],
  data: () => ({})
  ,
  methods: {
      postSearch: function(post) {
        this.$router.push({ path: "/post", query: {post: post}})
      },
      categorySearch: function(category) {
        this.$router.push({ path: "/search", query: {searchKeyword: category} })
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