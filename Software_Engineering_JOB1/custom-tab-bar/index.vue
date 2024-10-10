<!-- custom-tab-bar/index.vue -->
<template>
  <view class="tab-bar">
    <view
      v-for="(item, index) in list"
      :key="index"
      :class="['tab-bar-item', current === index ? 'active' : '']"
      @click="switchTab(index)"
    >
      <!-- 图标 -->
      <image
        v-if="item.iconPath"
        :src="current === index ? item.selectedIconPath : item.iconPath"
        class="tab-bar-icon"
      />
      <!-- 文字 -->
      <text class="tab-bar-text">{{ item.text }}</text>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      current: 0,
      list: [
        {
          pagePath: '/pages/home/home',
          iconPath: '/static/icons/home.png',
          selectedIconPath: '/static/icons/home_light.png',
          text: '首页'
        },
        {
          pagePath: '/pages/find_project/find_project',
          iconPath: '/static/icons/find_project.png',
          selectedIconPath: '/static/icons/find_project_light.png',
          text: '查找项目'
        },
        {
          pagePath: '/pages/message/message',
          iconPath: '/static/icons/message.png',
          selectedIconPath: '/static/icons/message_light.png',
          text: '消息'
        },
        {
          pagePath: '/pages/person/person',
          iconPath: '/static/icons/person.png',
          selectedIconPath: '/static/icons/person_light.png',
          text: '个人'
        }
      ]
    };
  },
  methods: {
    switchTab(index) {
      const url = this.list[index].pagePath;
      uni.switchTab({ url });
      this.current = index;
    }
  },
  created() {
    const pages = getCurrentPages();
    const currentPage = pages[pages.length - 1];
    const route = '/' + currentPage.route;
    this.list.forEach((item, index) => {
      if (item.pagePath === route) {
        this.current = index;
      }
    });
  }
};
</script>

<style>
.tab-bar {
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 120rpx; /* 设置 tabBar 的高度，可根据需要调整 */
  display: flex;
  background-color: rgba(91, 174, 183, 0.15); /* 设置背景颜色，透明度为 15% */
  border-top: 1px solid #eaeaea;
  z-index: 999;
}

.tab-bar-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.tab-bar-icon {
  width: 60rpx;
  height: 60rpx;
  margin-top: 10rpx; /* 调整图标与顶部的距离 */
  margin-bottom: 5rpx;
}

.tab-bar-text {
  font-size: 28rpx;
  color: #666666;
}

.active .tab-bar-text {
  color: #0094FF; /* 选中状态的文字颜色 */
}
</style>
