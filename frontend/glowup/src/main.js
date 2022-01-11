import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import axios from 'axios'
// import { datadogRum } from '@datadog/browser-rum';
// import winston from 'winston'


// datadogRum.init({
//     applicationId: 'bfeef476-f116-4c90-8bdb-af0aebcbf26d',
//     clientToken: 'pubecd3807f431c63820fa1a77ecaa757f3',
//     site: 'datadoghq.com',
//     service:'vue',
//     env:'staging',
//     // Specify a version number to identify the deployed version of your application in Datadog 
//     // version: '1.0.0',
//     sampleRate: 100,
//     trackInteractions: true,
//     allowedTracingOrigins: ["http://localhost"]
// });


// const logger = winston.createLogger({
//   level: 'info',
//   format: winston.format.json(),
//   defaultMeta: { service: 'user-service' },
//   transports: [
//     //
//     // - Write all logs with level `error` and below to `error.log`
//     // - Write all logs with level `info` and below to `combined.log`
//     //
//     new winston.transports.File({ filename: 'error.log', level: 'error' }),
//     new winston.transports.File({ filename: 'combined.log' }),
//   ],
// });

//
// If we're not in production then log to the `console` with the format:
// `${info.level}: ${info.message} JSON.stringify({ ...rest }) `
//
// if (process.env.NODE_ENV !== 'production') {
//   logger.add(new winston.transports.Console({
//     format: winston.format.simple(),
//   }));
// }

Vue.config.productionTip = false

new Vue({
  vuetify,
  axios,
  router,
  render: h => h(App)
}).$mount('#app')
