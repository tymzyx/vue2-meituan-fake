<template>
  <div>
    <location-city-head></location-city-head>
    <location-city-body></location-city-body>
  </div>
</template>

<script>
  import LocationCityHead from '../components/LocationCityHead'
  import LocationCityBody from '../components/LocationCityBody'

  export default {
    components: {LocationCityHead, LocationCityBody}
  }
</script>
