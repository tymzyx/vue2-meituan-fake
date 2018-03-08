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

  export default {
    components: {
      HomeHead,
      HomeBody,
      CommonFoot
    }
  }
</script>

