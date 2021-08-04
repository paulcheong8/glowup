<template>
  <v-app>
    <!-- <v-card
      class="overflow-hidden"
    >         -->
    <div v-if="mobileView">
      <NavbarMobile/>
    </div>

    <Navbar v-if="!mobileView"/>

    <div id="app">
      <router-view/>
    </div>

    <v-main>
      
      <!-- <HomePage/> -->
      <!-- <Footer/> -->
    </v-main>
    <!-- </v-card> -->
  </v-app>
</template>

<script>
import Navbar from './components/Navbar';
import NavbarMobile from './components/NavBarMobile';
// import Footer from './components/Footer';
// import HomePage from './pages/HomePage';

export default {
  name: 'App',

  data: () => ({
    mobileView: true,
    items: [
      { title: 'Home', icon: 'mdi-home-city' },
      { title: 'My Account', icon: 'mdi-account' },
      { title: 'Users', icon: 'mdi-account-group-outline' },
    ],    
  }),

  methods: {
    handleView() {
      this.mobileView = window.innerWidth <= 600;
    }
  },

  components: {
    Navbar,
    NavbarMobile,
    // Footer,
    // HomePage
  },

  created() {
    this.handleView();
  }

};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Montserrat:400,700,800');
@import url('https://fonts.googleapis.com/css?family=Nunito+Sans');

#app {
  font-family: "Montserrat" !important;
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  /* font-family: 'Nunito Sans' !important; */
  /* font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* background-color: #111e35; */
  background-color:rgba(255, 255, 255, 0.5);

  /* color: #2c3e50; */
  height: 100%;
}

body, html {
  padding: 0;
  margin: 0;
  width: 100%;
  min-height: 100vh;
}

body {
  /* background-color: #111e35; */
  background-color: white;
  /* background: #111e35; */
  background-color: white;
  /* border: 1px solid blue; */
}

#navigation-icon {
  padding: 10px 10px 20px;
  margin-right: 10px;
  cursor: pointer;

}


</style>