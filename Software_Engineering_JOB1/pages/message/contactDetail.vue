<template>
  <view class="chat-container">
    <!-- 联系人栏，固定在顶部 -->
    <view class="chat-header">
      <text class="contact-name">{{ contactName }}</text>
      <!-- 菜单图标 -->
      <image 
        class="menu-icon" 
        src="/static/icons/menu.png" 
        @click="toggleMenu" 
      />
      
      <!-- 下拉菜单 -->
      <view v-if="isMenuVisible" class="dropdown-menu">
        <view class="dropdown-item" @click="selectAction('申请加入')">申请加入</view>
        <view class="dropdown-item" @click="selectAction('邀请加入')">邀请加入</view>
      </view>

      <!-- 项目选择弹窗 -->
      <view v-if="isProjectSelectorVisible" class="project-selector">
        <view class="selector-header">
          <text>选择项目</text>
          <image 
            class="close-icon" 
            src="/static/icons/close.png" 
            @click="isProjectSelectorVisible = false" 
          />
        </view>
        <scroll-view class="project-list" scroll-y>
          <view 
            v-for="(project, index) in filteredProjects" 
            :key="index" 
            class="project-item" 
            @click="sendActionMessage(project)"
          >
            {{ project.name }}
          </view>
        </scroll-view>
      </view>
    </view>

    <!-- 消息内容区域，可滚动 -->
    <scroll-view 
      class="chat-content" 
      scroll-y 
      :scroll-with-animation="true" 
      :scroll-top="scrollTop" 
      @scrollToLower="onScrollToLower"
      ref="scrollView"
    >
      <view
        v-for="(message, index) in messages"
        :key="index"
        :class="['message', message.sender === 'me' ? 'message-right' : 'message-left']"
      >
        <image class="avatar" :src="message.sender === 'me' ? userAvatar : contactAvatar" />
        <view class="message-bubble">
          <text>{{ message.text }}</text>
        </view>
      </view>
    </scroll-view>

    <!-- 输入区域，固定在底部 -->
    <view class="chat-input">
      <input
        type="text"
        v-model="inputValue"
        placeholder="请输入消息..."
        class="input-box"
        @focus="scrollToBottom"
      />
      <button class="send-button" @click="sendMessage">发送</button>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      contactName: '',
      messages: [],
      inputValue: '',
      userAvatar: '/static/icons/user.png',
      contactAvatar: '/static/icons/contact.png',
      scrollTop: 0, // 用于控制滚动位置
      isMenuVisible: false, // 菜单是否可见
      isProjectSelectorVisible: false, // 项目选择弹窗是否可见
      selectedAction: '', // 当前选择的操作（申请加入或邀请加入）
      projects: [ // 示例项目列表
        { id: 1, name: '项目A' },
        { id: 2, name: '项目B' },
        { id: 3, name: '项目C' },
      ],
    };
  },
  computed: {
    filteredProjects() {
      // 根据选择的操作过滤项目列表，如果需要不同逻辑可以在这里处理
      return this.projects;
    }
  },
  onLoad(options) {
    if (options && options.name) {
      console.log(options);
      this.contactName = decodeURIComponent(options.name);
    }
  },
  methods: {
    sendMessage() {
      if (this.inputValue.trim() !== '') {
        this.messages.push({ sender: 'me', text: this.inputValue.trim() });
        this.inputValue = '';
        this.$nextTick(() => {
          this.scrollToBottom();
        });
      }
    },
    scrollToBottom() {
      // 延迟确保消息已渲染
      this.$nextTick(() => {
        const query = uni.createSelectorQuery().in(this);
        query.select('.chat-content').boundingClientRect();
        query.select('.chat-content').scrollOffset();
        query.exec((res) => {
          if (res[1]) {
            this.scrollTop = res[1].scrollHeight;
          }
        });
      });
    },
    onScrollToLower() {
      // 如果需要加载更多消息，可以在这里处理
      console.log('已滚动到最底部');
    },
    toggleMenu() {
      this.isMenuVisible = !this.isMenuVisible;
    },
    selectAction(action) {
      this.selectedAction = action;
      this.isMenuVisible = false;
      this.isProjectSelectorVisible = true;
    },
    sendActionMessage(project) {
      let messageText = '';
      if (this.selectedAction === '申请加入') {
        messageText = `申请加入项目：${project.name}`;
      } else if (this.selectedAction === '邀请加入') {
        messageText = `邀请加入项目：${project.name}`;
      }
      if (messageText) {
        this.messages.push({ sender: 'me', text: messageText });
        this.$nextTick(() => {
          this.scrollToBottom();
        });
      }
      this.isProjectSelectorVisible = false;
    }
  },
  watch: {
    messages() {
      this.scrollToBottom();
    }
  }
};
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100vh; /* 使容器占满整个视口高度 */
}

/* 联系人栏样式，固定在顶部 */
.chat-header {
  position: relative;
  padding: 15px;
  background-color: #ffffff;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  flex: 0 0 auto; /* 不允许增长或缩小 */
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 菜单图标样式 */
.menu-icon {
  position: absolute;
  right: 15px;
  width: 24px;
  height: 24px;
  cursor: pointer;
}

/* 下拉菜单样式 */
.dropdown-menu {
  position: absolute;
  top: 60px; /* 根据实际情况调整 */
  right: 15px;
  background-color: #ffffff;
  border: 1px solid #d1d1d1;
  border-radius: 5px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  z-index: 1000;
}

.dropdown-item {
  padding: 10px 20px;
  cursor: pointer;
}

.dropdown-item:hover {
  background-color: #f5f5f5;
}

/* 项目选择弹窗样式 */
.project-selector {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2000;
}

.project-selector .selector-header {
  width: 80%;
  background-color: #ffffff;
  padding: 15px;
  border-radius: 8px 8px 0 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.project-selector .close-icon {
  width: 24px;
  height: 24px;
  cursor: pointer;
}

.project-selector .project-list {
  width: 80%;
  max-height: 300px;
  background-color: #ffffff;
  border-radius: 0 0 8px 8px;
  overflow-y: auto;
}

.project-item {
  padding: 15px 20px;
  border-bottom: 1px solid #e0e0e0;
  cursor: pointer;
}

.project-item:hover {
  background-color: #f5f5f5;
}

/* 消息内容区域样式，可滚动 */
.chat-content {
  flex: 1 1 auto; /* 占据剩余空间 */
  padding: 10px;
  overflow-y: auto;
  background-color: #f5f5f5;
}

/* 消息样式 */
.message {
  display: flex;
  align-items: flex-end;
  margin-bottom: 10px;
}

.message-left {
  flex-direction: row;
}

.message-right {
  flex-direction: row-reverse;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin: 0 10px;
}

.message-bubble {
  max-width: 70%;
  padding: 10px;
  border-radius: 10px;
  background-color: #ffffff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.message-right .message-bubble {
  background-color: #2196f3;
  color: #ffffff;
}

/* 输入区域样式，固定在底部 */
.chat-input {
  display: flex;
  align-items: center; /* 垂直居中 */
  padding: 10px;
  border-top: 1px solid #e0e0e0;
  background-color: #f9f9f9;
  flex: 0 0 auto; /* 不允许增长或缩小 */
  box-sizing: border-box;
}

.input-box {
  flex: 1;
  padding: 10px;
  border: 1px solid #d1d1d1;
  border-radius: 25px;
  margin-right: 10px;
  background-color: #ffffff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  box-sizing: border-box;
  height: 40px; /* 固定高度 */
}

.send-button {
  padding: 0 15px;
  height: 40px; /* 与输入框相同的高度 */
  background-color: #2196f3;
  color: #ffffff;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: center;
}

@media (max-width: 600px) {
  .contact-name {
    font-size: 16px;
  }

  .input-box {
    padding: 8px;
    height: 36px; /* 调整小屏幕上的高度 */
  }

  .send-button {
    padding: 0 12px;
    height: 36px; /* 调整小屏幕上的高度 */
  }
}
</style>
