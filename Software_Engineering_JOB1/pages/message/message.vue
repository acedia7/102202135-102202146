<template>
  <view class="container">
    <view v-for="(group, index) in groups" :key="index" class="group-card" @click="toggleGroup(index)">
      <transition name="fade-slide">
        <view class="group-header">
          <view class="group-info">
            <image class="group-icon" src="/static/icons/group.png" />
            <text class="group-name">{{ group.name }}</text>
          </view>
          <image :class="['arrow-icon', { open: group.open }]" src="/static/icons/arrow.png" />
        </view>
      </transition>
      <transition name="slide">
        <view v-if="group.open" class="contact-list">
          <view v-if="group.contacts.length > 0">
            <view
              v-for="(contact, cIndex) in group.contacts"
              :key="cIndex"
              class="contact-item"
              @click.stop="navigateToContact(contact)"
            >
              <image class="contact-icon" src="/static/icons/contact.png" />
              <text class="contact-name">{{ contact }}</text>
            </view>
          </view>
          <view v-else class="no-contacts">
            <image class="no-contact-icon" src="/static/icons/no_contacts.png" />
            <text class="no-contact-text">暂无联系人</text>
          </view>
        </view>
      </transition>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      groups: [
        {
          name: '项目组1',
          open: false,
          contacts: ['洛杉机机长', '鸿运齐天'],
        },
        {
          name: '项目组2',
          open: false,
          contacts: ['勤始皇'],
        },
        {
          name: '项目组3',
          open: false,
          contacts: [],
        },
      ],
    };
  },
  methods: {
    toggleGroup(index) {
      this.groups[index].open = !this.groups[index].open;
    },
    navigateToContact(contact) {
      uni.navigateTo({
        url: `/pages/message/contactDetail?name=${encodeURIComponent(contact)}`,
      });
    },
  },
};
</script>

<style scoped>
.container {
  padding: 10px;
  background-color: #f5f5f5;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* 入口动画 */
.group-card {
  width: 100%;
  max-width: 600px;
  margin-bottom: 15px;
  background-color: #ffffff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transform: translateY(20px);
  opacity: 0;
  animation: fadeInUp 0.5s forwards;
}

/* 组头部 */
.group-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  background-color: #e0f0f1;
  color: #000000;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.group-header:hover {
  background-color: #e0f0f1;
  transform: scale(1.02);
}

.group-info {
  display: flex;
  align-items: center;
}

.group-icon {
  width: 24px;
  height: 24px;
  margin-right: 10px;
}

.group-name {
  font-size: 18px;
  font-weight: bold;
}

/* 箭头图标动画 */
.arrow-icon {
  width: 16px;
  height: 16px;
  transition: transform 0.3s;
}

.arrow-icon.open {
  transform: rotate(180deg);
}

/* 联系人列表 */
.contact-list {
  background-color: #f9f9f9;
  padding: 10px 20px;
  animation: fadeIn 0.3s forwards;
}

.contact-item {
  display: flex;
  align-items: center;
  padding: 10px 0;
  border-bottom: 1px solid #e0e0e0;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.contact-item:last-child {
  border-bottom: none;
}

.contact-item:hover {
  background-color: #e3f2fd;
  transform: translateX(5px);
}

.contact-icon {
  width: 20px;
  height: 20px;
  margin-right: 10px;
}

.contact-name {
  font-size: 16px;
  color: #333333;
}

/* 无联系人提示 */
.no-contacts {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px 0;
  color: #757575;
}

.no-contact-icon {
  width: 40px;
  height: 40px;
  margin-bottom: 10px;
}

.no-contact-text {
  font-size: 16px;
}

/* 动画效果 */
@keyframes fadeInUp {
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* 过渡效果 */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.3s ease;
}

.fade-slide-enter,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter,
.slide-leave-to {
  max-height: 0;
  opacity: 0;
  padding: 0 20px;
}

@media (max-width: 600px) {
  .group-header {
    padding: 12px 15px;
  }

  .group-name {
    font-size: 16px;
  }

  .contact-name {
    font-size: 14px;
  }

  .no-contact-text {
    font-size: 14px;
  }
}
</style>
