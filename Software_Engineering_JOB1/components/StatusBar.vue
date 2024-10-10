<!-- components/StatusBar.vue -->
<template>
  <view class="status-bar">
    <view class="status-content">
      <text class="time">12:00</text>
      <view class="status-icons">
        <image src="../static/icons/signal.png" class="icon-status"></image>
        <image src="../static/icons/wifi.png" class="icon-status"></image>
        <image src="../static/icons/battery.png" class="icon-status"></image>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  name: "StatusBar",
};
</script>

<style scoped>
.status-bar {
  height: 57px;
  background-color: #fff;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 10px;
  z-index: 999;
}

.status-content {
  display: flex;
  width: 100%;
  align-items: center;
  justify-content: space-between;
}

.time {
  font-size: 16px;
  color: #000;
}

.status-icons {
  display: flex;
  align-items: center;
}

.icon-status {
  width: 20px;
  height: 20px;
  margin-left: 5px;
}
</style>
