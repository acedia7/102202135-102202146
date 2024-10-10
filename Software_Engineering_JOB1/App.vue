<!-- App.vue -->
<template>
  <App>
    <slot></slot>
  </App>
</template>

<script>
export default {
  onLaunch: function () {
    console.log('App Launch');
  },
  onShow: function () {
    console.log('App Show');
  },
  onHide: function () {
    console.log('App Hide');
  },
};
</script>

<style>
	page{
		background-color: rgba(91, 174, 183, 0.05);
		min-height: 100vh; /* 确保背景覆盖整个屏幕高度 */
	}
</style>
