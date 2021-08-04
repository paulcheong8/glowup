<template>
    <div>
          <div class="d-flex align-center">
            <v-toolbar flat>
            <v-img
              class="shrink mr-2"
              contain
              src="../assets/lion.png"
              transition="scale-transition"
              width="40"
            />
            <span>
            <span> GLOW </span>
            <span class="font-weight-bold" style="color:#FFC850"> UP </span>
            </span>


            <v-spacer></v-spacer>

            <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
            </v-toolbar>
          </div>


          
          <v-navigation-drawer
            v-model="drawer"
            absolute
            right
            temporary
          >
            <v-list
              nav
              dense
            >
              <v-list-item-group
                v-model="group"
                active-class="deep-purple--text text--accent-4"
              >
                <v-list-item>
                  <v-list-item-icon>
                    <v-icon>mdi-account-group-outline</v-icon>
                  </v-list-item-icon>                  
                  <v-list-item-title>Join Us</v-list-item-title>
                </v-list-item>
      
                <v-list-item>
                  <v-list-item-icon>
                    <v-icon>mdi-account</v-icon>
                  </v-list-item-icon>                    
                  <v-list-item-title>Sign Up</v-list-item-title>
                </v-list-item>

                <v-list-item>
                  <v-list-item-icon>
                    <v-icon>mdi-forum</v-icon>
                  </v-list-item-icon>                    
                  <v-list-item-title>Contact us</v-list-item-title>
                </v-list-item>                

              </v-list-item-group>
            </v-list>
          </v-navigation-drawer>            
    </div>         

      
</template>



<script>
export default {
  data: () => ({
    drawer: false,
    group: null,  
  }),

  watch: {
    group() {
      this.drawer = false
    }
  },


};
</script>