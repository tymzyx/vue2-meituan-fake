
const mutations = {
  SET_CITY(state, city) {       // 设置当前城市
    state.selectedCity = city;
  },
  LOCATING_CITY(state, city) {  // 设置当前定位所在城市
    state.locatedCity = city;
  },
  UPDATE_RECENT_CITY(state) {
    let city = state.selectedCity;
    let cities = state.recentCities;
    if (city === state.locatedCity) {
      return;
    }
    for (let i of cities) {
      if (city === i) {
        return;
      }
    }
    cities.splice(0, 0, city);
    if (cities.length > 2) {
      cities.pop();
    }
  },
  SET_USERNAME(state, name) {
    state.username = name;
  }
}

export default mutations
