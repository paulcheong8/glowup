<template>
  <v-container>      
      <v-container class="my-10">
        <v-row justify="center" align="center" class="my-15">
            <v-card 
              elevation="0" 
              max-width="450" 
              class="text-left mr-15"
            >
              <v-card-title class="" style="font-size:3em;line-height:1">
                <!-- <p style="font-size:50px">Providing <span style="color:#A163F5">Better </span>Transport</p> -->
                <span style="padding-right:10px">Be Your</span> <span style="color:orange;">Genuine </span>Self
              </v-card-title> 
              <v-card-text style="font-size:1em">
                  A place for everyone from different walks of life to come together and help one another through their journeys. 
              </v-card-text>    
            </v-card>

            <v-card elevation="0">
            <v-img
              :src="require('../assets/lion.png')"
              
              max-height="400"
              max-width="300"
            />            
            </v-card>                  
        </v-row>
        <v-row justify="center">
        <v-img
            :src="require('../assets/more.png')"            
            max-height="100"
            max-width="50"
        >

        </v-img>
        </v-row>        
        
      </v-container>

      <v-container class="my-10">
        <v-row justify="center" align="center" class="">
            <v-card elevation="0">
            <v-img
              :src="require('../assets/pawprint.png')"
              
              max-height="350"
              max-width="250"
              class="mr-15"
            />            
            </v-card>   
                      
            <v-card 
              elevation="0" 
              max-width="450" 
              class="text-left"
            >

              As we manoeuvre through this important part of our life, we may face bumps on the road; 
              some of which we have the answers to, and some we don't. <br><br>We will definitely face failures
              that we may be uncomfortable to share in fear of judgement. On social media, we only see the 
              success and greatness of people and their experiences. But what about failure? 
            </v-card>
               
        </v-row>
        <v-row justify="center">
        <v-img
            :src="require('../assets/more.png')"            
            max-height="100"
            max-width="50"
            class="my-10"          
        >

        </v-img>
        </v-row>

        <v-row justify="center" align="center" class="">
                      
            <v-card 
              elevation="0" 
              max-width="450" 
              class="text-right mr-15"
            >
            We hope this can be a place where we can help one another find the questions we are looking 
            for, where we can be vulnerable and share our failures so that others can learn from it.
            </v-card>
            <v-card elevation="0">
            <v-img
              :src="require('../assets/cub.png')"
              
              max-height="350"
              max-width="250"
            />            
            </v-card>              
               
        </v-row>
        <v-row justify="center">
        <v-img
            :src="require('../assets/more.png')"            
            max-height="100"
            max-width="50"
            class="my-3"          
        >

        </v-img>
        </v-row>

      </v-container>      


      <v-col
        cols="12"
        class="mb-10"
      >
     
          <p class="mb-10" style="font-size:3em">
            What is our <span style="color:orange"> purpose </span>
          </p>          

          <v-row justify="center" class="my-5">
            <!-- <v-col> -->
              
              <v-card 
              v-for="(benefit, i) in benefits"
              :key=i
              class="mx-10" 
              max-width="300" 
              height="400"              
              >
                <br>
                <v-img
                :src="require(`../assets/${benefit.src}`)"
                max-width="150"
                class="mx-auto mb-5"
                >
                </v-img
                >            
                <v-card-title class="font-weight-bold" style="color:orange">
                  <p class="mx-auto" style="font-size:25px">
                    {{benefit.title}}  
                  </p>
                </v-card-title>
                <v-card-subtitle>
                  {{benefit.text}}
                </v-card-subtitle>  
              </v-card>
          
            <!-- </v-col> -->
          </v-row>
      </v-col>      



      <v-row class=""> 
      <v-col
        class="mb-5"
        cols="12"
      >
        <p class="mb-10" style="font-size:3em">
          What you can <span style="color:orange"> do </span>
        </p>

        <v-row justify="center" >
          <v-card 
          v-for="(next, i) in whatYouCanDo"
          :key=i
          max-width="275" 
          
          class="mx-1 elevation-0 my-10"
          > 
              <v-row>              
                <v-img
                :src="require(`../assets/${next.src}`)"
                max-width="150"
                class="mb-10 mx-auto"
                />
              </v-row>            
              <v-row justify="center">
                <v-avatar
                color="orange"
                size="25"
                class="mb-3"
                >
                <span style="color:white">{{i + 1}}</span>
                </v-avatar>
              </v-row>
              <v-row>
                <p class="mx-10">
                {{next.text}}
                </p>
              </v-row>
          </v-card>

        

        </v-row>
      </v-col>
      </v-row>



  </v-container>
</template>

<script>

  export default {

    name: 'AboutPage',

    data: () => ({
      whatYouCanDo: [
        {
          text: 'Search for topics or areas of interest',
          // src: '/img/building.9e1811b7.png'
          src: "magnifying-glass.png"
        },        
        {
          text: 'Ask for advice',
          // src: '/img/computer.dc3c76ba.png'
          src: "faq.png"
        },
        {
          text: 'Share your journal (if you are comfortable with it)',
          // src: '/img/route.26f3f59b.png'
          src: "journal.png"
        },
        {
          text: 'Give advice or leave well meaning thoughts',
          // src: '/img/bus.c2f2fcb7.png'
          src: "lightbulb.png"
        }
      ],
      benefits: [
        {
          title: 'Build Communities',
          text: "We want to this to be a place where you can find like-minded people for support and advice.",
          src: "teamwork.png"
        },
        {
          title:'Embrace Failure',
          text: "Unlike other platforms where you only see how successful someone is or how great an experience someone had, let's share our failures and tide through it together.",
          src: "success.png"
        },
        {
          title: 'Learn Together',
          text: "From the experiences of our community, we can learn from their mistakes and failures to emerge stronger and achieve what we set out for ourselves.",
          src: "idea.png"
        }
      ],
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
      busStops: []      
    }),

  }
</script>

<style>
  .screenFiller {
      height:100vh;

  }

  .chevronbody {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    width: 100%;
    height: 100%;
    /* background: rgba(99, 94, 94, 0.1); */
  }

  .chevron {
    position: absolute;
    width: 28px;
    height: 8px;
    opacity: 0;
    transform: scale3d(0.5, 0.5, 0.5);
    animation: move 3s ease-out infinite;
  }

  .chevron:first-child {
    animation: move 3s ease-out 1s infinite;
  }

  .chevron:nth-child(2) {
    animation: move 3s ease-out 2s infinite;
  }

  .chevron:before,
  .chevron:after {
    content: ' ';
    position: absolute;
    top: 0;
    height: 100%;
    width: 51%;
    background: #37474F;
  }

  .chevron:before {
    left: 0;
    transform: skew(0deg, 30deg);
  }

  .chevron:after {
    right: 0;
    width: 50%;
    transform: skew(0deg, -30deg);
  }

  @keyframes move {
    25% {
      opacity: 1;

    }
    33% {
      opacity: 1;
      transform: translateY(30px);
    }
    67% {
      opacity: 1;
      transform: translateY(40px);
    }
    100% {
      opacity: 0;
      transform: translateY(55px) scale3d(0.5, 0.5, 0.5);
    }
  }

  @keyframes pulse {
    to {
      opacity: 1;
    }
  }
</style>