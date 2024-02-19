<template>
  <!--img alt="Vue logo" src="./assets/logo.png"-->
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <ElementTest msg="Welcome to Your Vue.js App"/>
  <BeiAn msg="Welcome to Your Vue.js App"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import ElementTest from './components/ElementTest.vue'
import BeiAn from './components/BeiAn.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    ElementTest,
	BeiAn
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
  margin-top: 60px;
}
</style>
