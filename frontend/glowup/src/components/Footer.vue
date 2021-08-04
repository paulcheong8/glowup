<template>
    <v-footer dark padless color="#A163F5">
    <v-col
        class="text-center"
        cols="12"
    >
        <v-btn
        v-for="icon in icons"
        :key="icon"
        class="mx-4 my-3 white--text"
        icon
        >
        <v-icon size="24px">
            {{ icon }}
        </v-icon>
        </v-btn>  

        <v-divider></v-divider>
        <p class="my-3">
        <strong>Ride Together</strong> — {{ new Date().getFullYear() }} 
        </p>
        
    </v-col>
    </v-footer>     
</template>

<script>
export default {
  data: () => ({
    icons: [
      'mdi-facebook',
      'mdi-twitter',
      'mdi-linkedin',
      'mdi-instagram',
    ],
  }),    
}
</script>