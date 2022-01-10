<template>
    <v-card
      class="mx-auto my-10"
      max-width="800"
      outlined
    >
      <v-card-text class="overline">
        <!-- <div class="text-overline"> -->
          <strong>What advice do you need?</strong>
        <!-- </div> -->
      </v-card-text>

      <v-dialog
        v-model="dialog"
        persistent
        max-width="600px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="amber darken-1"
            dark
            v-bind="attrs"
            v-on="on"
            text
            outlined
          >
            Start a question
          </v-btn>
        </template>
        <v-form
          ref="form"
          v-model="valid"
        >        
          <v-card>
            <v-card-title>
              <span class="text-h5">Ask a question</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>

                    <v-col
                      cols="12"
                    >
                      <v-text-field
                        v-model= "nickname"
                        :rules="formRules"
                        label="Nickname*"
                        required
                        color="amber darken-1"
                      ></v-text-field>
                    </v-col>

                    <v-col cols="12">
                      <v-text-field
                        v-model= "title"
                        :rules="formRules"
                        label="Title of question*"
                        required
                        color="amber darken-1"
                      ></v-text-field>
                    </v-col>

                    <v-col cols="12">
                      <v-textarea
                        v-model= "advice"
                        :rules="formRules"
                        name="input-7-1"
                        color="amber darken-1"
                        label="What advice do you need?*"
                        auto-grow
                      >
                      </v-textarea>
                    </v-col>
                    <!-- <v-col cols="12">
                      <v-text-field
                        v-model="organisation"
                        :rules="formRules"
                        label="Organisation*"
                        required
                        color="amber darken-1"
                      ></v-text-field>
                    </v-col> -->
                    <v-col
                      cols="12"
                      sm="6"
                    >
                      <v-autocomplete
                        v-model="selectedCategory"
                        :rules="formRules"
                        :items=categories
                        label="Category"                        
                        
                        required
                      ></v-autocomplete>
                    </v-col>
                </v-row>
              </v-container>
              <small>*indicates required field</small>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="amber darken-1"
                text
                @click="dialog = false"
              >
                Close
              </v-btn>
              <v-btn
                :disabled="!valid"
                color="amber darken-1"
                text
                @click=getAdviceQuery
              >
                Post
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
      </v-dialog>


    </v-card>      
</template>

<script>
import axios from 'axios'

export default {
  props: ['posts'],
  data: function () {
      return {
      dialog: false,
      valid: true,
      nickname: "",
      title: "",
      advice: "",
      selectedCategory: "",     
      formRules: [
        v => !!v || 'This field is required',
      ],
      categories: ['Technology', 'Finance', 'Internship', 'Graduate Program', 'Traineeship', 'Career', 'Misc'],
    
      }
  
  },

  methods: {
      getAdviceQuery: function() {
        let adviceObj = {
          nickname: this.nickname,
          timePosted: "1d ago",
          selectedCategory: this.selectedCategory,
          title: this.title,
          advice: this.advice,
          numViews: 200,
          numComments: 20,
          datetime: new Date().getTime()
        }

        let url = 'http://ec2-3-237-88-193.compute-1.amazonaws.com/createpost/'
        axios.post(
          url,
          adviceObj,
          { headers: {
              "Content-Type": "application/json",
              // 'Access-Control-Allow-Origin': '*',
              // "Access-Control-Allow-Methods": "*",
              // "Access-Control-Allow-Headers": "*",
              } 
          }
        )
        .then(response => console.log(response.status))

        this.posts.push(adviceObj)
        this.dialog = false;
      },      
  }    
}
</script>