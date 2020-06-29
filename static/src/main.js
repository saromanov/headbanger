import Vue from 'vue'
import App from './App.vue'

new Vue({
  el: '#app',
  render: h => h(App),
  data: () => ({
    message: new Date(),
  }),
  methods:{
    createBranch:() => {
      console.log("MESSAGE: ", this.message);
      const path = 'http://localhost:5000/api/branches';
      axios.post(path, {
        name: this.branch_name,
      }).then((res) => {
        console.log('FINE');
      }).catch((error) => {
        console.error(error);
      })
    },
  }
});
