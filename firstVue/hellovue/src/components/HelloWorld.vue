<template>
  <div class="hello">
    <!--这里注销了原来的一段话zy
    <h1>{{ msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
	-->
    <h3>日常工具（Vue）</h3>
    <ul>
      <li><a href="https://www.bilibili.com/" target="_blank" rel="noopener">bilibili</a></li>
      <li><a href="https://filehelper.weixin.qq.com/" target="_blank" rel="noopener">微信传输</a></li>
      <li><a href="https://mail.163.com/" target="_blank" rel="noopener">网易邮箱</a></li>
      <li><a href="https://fanyi.youdao.com/" target="_blank" rel="noopener">有道翻译</a></li>
      <li><a href="https://pc.qq.com/" target="_blank" rel="noopener">腾讯软件中心</a></li>
      <li><a href="http://vue1.bbkkk.top/" target="_blank" rel="noopener">个人vue页</a></li>
    </ul>
  </div>
</template>

<script >
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

