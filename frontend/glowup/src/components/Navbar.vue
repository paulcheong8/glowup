<template>
    <nav>
    <v-app-bar
      app
      absolute
      color="white"
      elevate-on-scroll
      scroll-target="#scrolling-techniques-7"
    >
      <div class="d-flex align-center">

          <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

        <v-img
          class="shrink mr-2"
          contain
          src="../assets/lion.png"
          transition="scale-transition"
          width="40"
        />
        <v-toolbar-items @click="$router.push('/')" style="cursor:pointer">
        <span> GLOW </span>
        <span class="font-weight-bold" style="color:#FFC850"> UP </span>
        </v-toolbar-items>

      </div>

      <v-card
        class="ma-10"
        flat      
        width="300"
      >
        <v-text-field
          v-model="search"
          hide-details
          label="Seek and you shall find"
          prepend-icon="mdi-magnify"
          single-line
          rounded
          filled
          dense
          color="amber darken-1"
          @keydown.enter="handleSearch"
        ></v-text-field>    
      </v-card>

      <v-spacer></v-spacer>

      <!-- login dialogue -->
      <v-dialog
        v-model="loginDialog"
        persistent
        max-width="450px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            small
            color="amber darken-2"
            elevation="0"
            v-bind="attrs"
            v-on="on"
            dark
            rounded
            class="mr-3"
          >
            Login
          </v-btn>
        </template>
        <v-form
          ref="form"
          v-model="valid"
        >        
          <v-card>
            <v-card-title>
              <span class="text-h5">Login</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>

                    <v-col
                      cols="12"
                    >
                      <v-text-field
                        v-model= "email"
                        :rules="formRules"
                        label="Email"
                        required
                        color="amber darken-1"
                      ></v-text-field>
                    </v-col>

                    <v-col cols="12">
                      <v-text-field
                        v-model= "password"
                        :append-icon="showLoginPassword ? 'mdi-eye' : 'mdi-eye-off'"
                        :type="showLoginPassword ? 'text' : 'password'"
                        name="input-10-1"
                        :rules="formRules"
                        label="Password"
                        required
                        color="amber darken-1"
                        @click:append="showLoginPassword = !showLoginPassword"
                      ></v-text-field>
                    </v-col>

                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="amber darken-1"
                text
                @click="loginDialog = false"
              >
                Close
              </v-btn>
              <v-btn
                :disabled="!valid"
                color="amber darken-1"
                text
                @click=login
              >
                Login
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
      </v-dialog>      

      <!-- signup dialogue -->
      <v-dialog
        v-model="signupDialog"
        persistent
        max-width="450px"
        
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            small
            color="amber darken-4"
            elevation="0"
            v-bind="attrs"
            v-on="on"
            dark
            rounded
            class="mr-3"            
          >
            Sign Up
          </v-btn>
        </template>
        <v-form
          ref="form"
          v-model="valid"
        >        
          <v-card>
            <v-card-title>
              <span class="text-h5">Sign Up</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>

                    <v-col
                      cols="12"
                    >
                      <v-text-field
                        v-model= "nickname"
                        :rules="nicknameRules"
                        :counter="15"
                        label="Nickname"
                        required
                        color="amber darken-1"
                      ></v-text-field>
                    </v-col>
                    
                    <v-col
                      cols="12"
                    >
                      <v-text-field
                        v-model= "email"
                        :rules="emailRules"
                        label="Email"
                        required
                        color="amber darken-1"
                      ></v-text-field>
                    </v-col>

                    <v-col cols="12">
                      <v-text-field
                        v-model= "password"
                        :append-icon="showSignupPassword ? 'mdi-eye' : 'mdi-eye-off'"
                        :type="showSignupPassword ? 'text' : 'password'"
                        name="input-10-1"
                        :rules="passwordRules"
                        label="Password"
                        required
                        color="amber darken-1"
                        @click:append="showSignupPassword = !showSignupPassword"
                      ></v-text-field>
                    </v-col>

                    <v-col cols="12">
                      <v-text-field
                        v-model= "confirmPassword"
                        :append-icon="showSignupConfirmPassword ? 'mdi-eye' : 'mdi-eye-off'"
                        :type="showSignupConfirmPassword ? 'text' : 'password'"
                        name="input-10-1"
                        :rules="confirmPasswordRules.concat(passwordConfirmationRule)"
                        label="Confirm Password"
                        required
                        color="amber darken-1"
                        @click:append="showSignupConfirmPassword = !showSignupConfirmPassword"
                      ></v-text-field>
                    </v-col>                    

                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="amber darken-1"
                text
                @click="signupDialog = false"
              >
                Close
              </v-btn>
              <v-btn
                :disabled="!valid"
                color="amber darken-1"
                text
                @click=signup
              >
                signup
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
      </v-dialog>   

  
      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        icon
        large
        color="#FFC850"
      >
        <v-icon>mdi-bell-outline</v-icon>
      </v-btn>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        icon
        large
        color="#FFC850"
      >
        <!-- <span class="mr-2">Join Us</span> -->
        <v-icon>mdi-account</v-icon>
      </v-btn>      

    
    </v-app-bar>    

    
    <v-navigation-drawer
      v-model="drawer"
      temporary
      absolute      
    >
      <v-list nav dense>
        <v-list-item          
          v-for="item in categoryItems" 
          :key="item.title"
          active-class="highlighted"
          :to="item.path"
          :class="item.path === $route.path ? 'highlighted' : ''"
        >
            <v-icon> {{item.icon}} </v-icon>
          
            <v-list-item-title>
            {{ item.title }}
            </v-list-item-title>
          


        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    </nav>


</template>

<script>
export default {
  data: () => ({
    loginDialog: false,
    signupDialog: false,
    showLoginPassword: false,
    showSignupPassword: false,
    showSignupConfirmPassword: false,
    nickname: "",
    email: "",
    password: "",
    confirmPassword: "",
    valid: true,
    search: "",
    formRules: [
      v => !!v || 'This field is required',
    ],    
    passwordRules: [
      v => !!v || 'Password is required',
    ],
    confirmPasswordRules: [
      v => !!v || "Password is required",
    ],
    nicknameRules: [
      v => !!v || 'Nickname is required',
      v => v.length <= 15 || 'Nickname must be less than 15 characters',
    ],        
    emailRules: [
      v => !!v || 'Email is required',
      v => /.+@.+/.test(v) || 'Email must be valid',
    ],
    drawer: false,
    categoryItems: [
      { title: "Home", icon:"mdi-home-outline", path: "/"},
      { title: "About", icon:"mdi-information-outline", path: "/about"},
      { title: "Experiences", icon:"mdi-book-open-outline", path: "/experiences"},
      { title: "Technology", icon:"mdi-code-braces", path: "/technology"},
      { title: "Finance", icon:"mdi-chart-line", path: "/finance"},
      { title: "Internship", icon:"mdi-baby-face-outline", path: "/internship"},
      { title: "Graduate Program", icon:"mdi-school-outline", path: "/graduate"},
      { title: "Traineeship", icon:"mdi-arm-flex-outline", path: "/traineeship"},
      { title: "Career", icon:"mdi-briefcase-outline", path: "/career"},
      { title: "Misc", icon:"mdi-dots-horizontal", path: "/misc"},
    ]

  }),

  // watch: {
  //   group() {
  //     this.drawer = false
  //   }
  // },  

  methods: {
    login: function() {
      console.log(this.password)
      console.log(this.email)
      this.loginDialog = false;
    },

    signup: function() {
      console.log(this.password)
      console.log(this.email)
      this.signupDialog = false;
    },

    handleSearch: function() {
      console.log(this.search);
      this.$router.push({ path: "/search", query: {searchKeyword: this.search} })
    },

    categorySearch: function(category) {
      this.$router.push({ path: "/search", query: {searchKeyword: category} }).catch(()=>{})
    },

  },

  computed: {
    passwordConfirmationRule() {
      return () =>
        this.password === this.confirmPassword || "Password must match";
    }
  },

};
</script>
