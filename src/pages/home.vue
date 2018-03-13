<template>
  <div>
    <home-head></home-head>
    <home-body></home-body>
    <common-foot activeKey="0"></common-foot>
  </div>
</template>

<script>
  import HomeHead from '../components/HomeHead'
  import HomeBody from '../components/HomeBody'
  import CommonFoot from '../components/CommonFoot'

  import {getCookie} from '../assets/js/cookie'
  import {mapState, mapMutations} from 'vuex'

  export default {
    components: {
      HomeHead,
      HomeBody,
      CommonFoot
    },
    computed: {
      ...mapState(['username'])
    },
    methods: {
      ...mapMutations({
        setUsername: 'SET_USERNAME',
      })
    },
    mounted() {
      if (this.username) {
        return;
      }
      let _this = this;
      let token = getCookie('token');
      if (token) {
        this.$http.post('http://localhost:7766/api/isLogin', {
        token: token
      })
        .then(function (response) {
          console.log(response);
          let result = response.data;
          if (result.success) {
            _this.setUsername(result.username);
          } else {
            _this.setUsername('');
          }
        })
        .catch(function (error) {
          console.log('error: ', error);
        });
      }
    }
  }
</script>

