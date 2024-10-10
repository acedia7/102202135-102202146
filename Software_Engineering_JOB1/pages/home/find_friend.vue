<template>
  <view class="recommend-list-container">
    <scroll-view class="recommend-list" scroll-y>
      <view v-for="(user, index) in users" :key="index" class="info-card">
        <!-- 左侧：头像 -->
        <image :src="user.avatar" class="avatar" />

        <!-- 中部：用户信息 -->
        <view class="user-info">
          <!-- 姓名 -->
          <text class="user-name">{{ user.name }}</text>

          <!-- 专业 -->
          <text class="user-major">专业: {{ user.major }}</text>

          <!-- 兴趣领域 -->
          <text class="user-skills">技能: {{ user.skills }}</text>
        </view>

        <!-- 右侧：私聊按钮 -->
        <button class="chat-button" @click="startChat(user)">
          <image class="chat-icon" src="/static/icons/chat.png" />
          <text class="chat-text">私聊</text>
        </button>
      </view>
    </scroll-view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      users: [
        { name: '洛杉矶机长', major: '航天工程', skills: '打篮球, 开飞机', avatar: '/static/avatars/user1.jpg' },
        { name: '妈妈生的', major: '烟草品质分析', skills: '烟草调制, 养雪豹', avatar: '/static/avatars/user2.jpg' },
        { name: '我给你补个蛋', major: '播音主持', skills: '卖鸡蛋, 开大奔', avatar: '/static/avatars/user3.jpg' },
		{ name: '洛杉矶机长', major: '航天工程', skills: '打篮球, 开飞机', avatar: '/static/avatars/user1.jpg' },
		{ name: '妈妈生的', major: '烟草品质分析', skills: '烟草调制, 养雪豹', avatar: '/static/avatars/user2.jpg' },
		{ name: '我给你补个蛋', major: '播音主持', skills: '卖鸡蛋, 开大奔', avatar: '/static/avatars/user3.jpg' },
		{ name: '洛杉矶机长', major: '航天工程', skills: '打篮球, 开飞机', avatar: '/static/avatars/user1.jpg' },
		{ name: '妈妈生的', major: '烟草品质分析', skills: '烟草调制, 养雪豹', avatar: '/static/avatars/user2.jpg' },
		{ name: '我给你补个蛋', major: '播音主持', skills: '卖鸡蛋, 开大奔', avatar: '/static/avatars/user3.jpg' },
		{ name: '洛杉矶机长', major: '航天工程', skills: '打篮球, 开飞机', avatar: '/static/avatars/user1.jpg' },
		{ name: '妈妈生的', major: '烟草品质分析', skills: '烟草调制, 养雪豹', avatar: '/static/avatars/user2.jpg' },
		{ name: '我给你补个蛋', major: '播音主持', skills: '卖鸡蛋, 开大奔', avatar: '/static/avatars/user3.jpg' },
		{ name: '洛杉矶机长', major: '航天工程', skills: '打篮球, 开飞机', avatar: '/static/avatars/user1.jpg' },
		{ name: '妈妈生的', major: '烟草品质分析', skills: '烟草调制, 养雪豹', avatar: '/static/avatars/user2.jpg' },
		{ name: '我给你补个蛋', major: '播音主持', skills: '卖鸡蛋, 开大奔', avatar: '/static/avatars/user3.jpg' }
      ]
    };
  },
  methods: {
    startChat(user) {
      // 开始私聊逻辑
      uni.showToast({
        title: `与 ${user.name} 私聊功能待实现`,
        icon: 'none'
      });
    }
  }
};
</script>

<style scoped>
.recommend-list-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #f0f2f5;
  padding: 10px;
}

.recommend-list {
  flex: 1;
}

.info-card {
  display: flex;
  align-items: center;
  background-color: #ffffff;
  border-radius: 12px;
  padding: 15px;
  margin-bottom: 15px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  width: 100%;
  box-sizing: border-box;
}

.avatar {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  object-fit: cover;
  margin-right: 15px;
}

.user-info {
  display: flex;
  flex-direction: column;
  flex: 1;
}

.user-name{
	font-size: 20px;
	color: #333333;
	margin-bottom: 4px;
}

.user-major,
.user-skills {
  font-size: 15px;
  color: #333333;
  margin-bottom: 4px;
}

.user-name {
  font-weight: bold;
}

.chat-button {
  display: flex;
  align-items: center;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  font-size: 14px;
  outline: none;
}

.chat-icon {
  width: 16px;
  height: 16px;
  margin-right: 5px;
}

.chat-text {
  color: #027373;
}
</style>