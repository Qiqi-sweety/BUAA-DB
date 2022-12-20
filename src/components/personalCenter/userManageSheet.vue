<!-- personalCenter的子组件：用户的账号管理 -->

<template>
    <NCard style = "width:1390px;margin-left:30px">
      <h3 style = "font-size: 30px;margin-top: 0%;margin-left:20px">个人信息</h3>
      <el-divider/>
        <el-row>
          <el-col :span="6">
            <p style = "font-size: 25px;margin-left: 150px;">头像</p>
          </el-col>
          <el-col :span="1">
            <el-divider direction="vertical" style="height:80px;margin-top:10px"/>
          </el-col>
          <el-col :span="11">
            <img src="../../assets/card.jpg" style = "width: 85px;height: 85px;">
          </el-col>
          <el-col :span="6">
            <n-upload action="/api/image/update/">
              <n-button disabled type="warning" size = "large" round style = "width: 100px;margin-left:100px;margin-top: 25px;">
                修改
              </n-button>
            </n-upload>            
          </el-col>
        </el-row>
      <el-divider/>
        <el-row>
          <el-col :span="6">
            <p style = "font-size: 25px;margin-left: 130px;">用户名</p>
          </el-col>
          <el-col :span="1">
            <el-divider direction="vertical" style="height:80px;margin-top:10px"/>
          </el-col>
          <el-col :span="11">
            <p 
            style = "font-size:20px;color:gray;margin-top: 30px;">
              {{info.user_info.name}}
            </p>
          </el-col>
          <el-col :span="6">
            <n-button type="warning" size = "large" round 
            style = "width: 100px;margin-left:100px;margin-top: 25px;"
            @click="showIdModal = true">
            修改
            </n-button>
          </el-col>
        </el-row>
      <el-divider/>
        <el-row>
          <el-col :span="6">
            <p style = "font-size: 25px;margin-left: 150px;">地址</p>
          </el-col>
          <el-col :span="1">
            <el-divider direction="vertical" style="height:80px;margin-top:10px"/>
          </el-col>
          <el-col :span="11">
            <p 
            style = "font-size:20px;color:gray;margin-top: 30px;">
              {{info.user_info.address}}
            </p>
          </el-col>
          <el-col :span="6">
            <n-button type="warning" size = "large" round 
            style = "width: 100px;margin-left:100px;margin-top: 25px;"
            @click="showAddressModal = true">
            修改
            </n-button>
          </el-col>
        </el-row>
      <el-divider/>
        <el-row>
          <el-col :span="6">
            <p style = "font-size: 25px;margin-left: 130px;">银行卡</p>
          </el-col>
          <el-col :span="1">
            <el-divider direction="vertical" style="height:80px;margin-top:10px"/>
          </el-col>
          <el-col :span="11">
            <p 
            style = "font-size:20px;color:gray;margin-top: 30px;">
              {{info.user_info.card_num}}
            </p>
          </el-col>
          <el-col :span="6">
            <n-button type="warning" size = "large" round 
            style = "width: 100px;margin-left:100px;margin-top: 25px;"
            @click="showCardModal = true"
            >
            换绑
            </n-button>
          </el-col>
        </el-row>
      <el-divider/>
        <el-row>
          <el-col :span="6">
            <p style = "font-size: 25px;margin-left: 150px;">密码</p>
          </el-col>
          <el-col :span="1">
            <el-divider direction="vertical" style="height:80px;margin-top:10px"/>
          </el-col>
          <el-col :span="5">
            <p
                style = "font-size:20px;color:gray;margin-top: 30px;">
              ******
            </p>
          </el-col>
          <el-col :span="6"><div class="grid-content ep-bg-purple" /></el-col>
          <el-col :span="6">
            <n-button type="warning" size = "large" round 
            style = "width: 100px;margin-left:100px;margin-top: 25px;"
            @click="showPasswordModal = true"
            >
            修改
            </n-button>
          </el-col>
        </el-row>
    </NCard>

    <n-modal
    v-model:show="showIdModal"
    preset="card"
    title="修改用户名"
    style="width:400px;height:250px"
    :bordered="false"
    >
        <n-card
        style="width: 350px"
        :bordered="false"
        size="huge"
        role="dialog"
        aria-modal="true"
        >
        <el-input
          v-model="info.new_info.name"
          type="name"
          size = "large"
          placeholder="请输入新用户名"
          maxlength="20"
          style = "margin-bottom: 40px;"
        >
        
          <template #prefix>
            <el-icon class="el-input__icon"><user /></el-icon>
          </template>
        </el-input>
        <n-button style = "margin-left:80px;" size = "large" round type="warning" @click="changeName">
        确认修改
        </n-button>  
    </n-card>
  </n-modal>

  <n-modal
    v-model:show="showAddressModal"
    preset="card"
    title="修改地址"
    style="width:400px;height:250px"
    :bordered="false"
    >
        <n-card
        style="width: 350px"
        :bordered="false"
        size="huge"
        role="dialog"
        aria-modal="true"
        >
        <el-input
          v-model="info.new_info.address"
          type="name"
          size = "large"
          placeholder="请输入新地址"
          style = "margin-bottom: 40px;"
        >
        
          <template #prefix>
            <el-icon class="el-input__icon"><position /></el-icon>
          </template>
        </el-input>
        <n-button style = "margin-left:80px;" size = "large" round type="warning" @click="changeAddr">
        确认修改
        </n-button>  
    </n-card>
  </n-modal>

  <n-modal
    v-model:show="showCardModal"
    preset="card"
    title="更换银行卡"
    style="width:400px;height:250px"
    :bordered="false"
  >
        <n-card
        style="width: 350px"
        :bordered="false"
        size="huge"
        role="dialog"
        aria-modal="true"
        >
        <el-input
          v-model="info.new_info.card_num"
          type="name"
          size = "large"
          placeholder="请输入新银行卡号"
          style = "margin-bottom: 40px;"
        >
        
          <template #prefix>
            <el-icon class="el-input__icon"><CreditCard /></el-icon>
          </template>
        </el-input>
        <n-button style = "margin-left:80px;" size = "large" round type="warning" @click="changeCard">
        确认修改
        </n-button>  
    </n-card>
  </n-modal>

  <n-modal
    v-model:show="showPasswordModal"
    preset="card"
    title="修改密码"
    style="width:400px;"
    :bordered="false"
    >
<!--        <n-card-->
<!--        style="width: 350px"-->
<!--        :bordered="false"-->
<!--        size="huge"-->
<!--        role="dialog"-->
<!--        aria-modal="true"-->
<!--        >-->
          <el-form
              :model="pw"
              :rules="rules"
              status-icon
              style="width: 350px;"
          >
            <el-form-item prop="oldPw">
              <el-input
                  v-model="pw.oldPw"
                  type="password"
                  placeholder="输入旧密码"
                  show-password
                  size = "large"
              >
                <template #prefix>
                  <el-icon class="el-input__icon"><lock /></el-icon>
                </template>

              </el-input>
            </el-form-item>
            <el-form-item prop="newPw">
              <el-input
                v-model="pw.newPw"
                type="password"
                placeholder="设置新密码"
                show-password
                size = "large"
                minlength="6"
              >
                <template #prefix>
                  <el-icon class="el-input__icon"><lock /></el-icon>
                </template>

              </el-input>
            </el-form-item>
            <el-form-item prop="confirmPw">
              <el-input
                v-model="pw.confirmPw"
                type="password"
                placeholder="确认新密码"
                show-password
                size = "large"
              >
                <template #prefix>
                  <el-icon class="el-input__icon"><lock /></el-icon>
                </template>

              </el-input>
            </el-form-item>
            <el-form-item>
              <n-button style = "margin-left:80px; margin-top: 30px;"
                        size = "large" round type="warning" @click="changePw">
                确认修改
              </n-button>
            </el-form-item>
          </el-form>
  

<!--    </n-card>-->
  </n-modal>


</template>

<script setup>
import {onMounted, reactive, ref} from 'vue'
import {NCard,NButton,NModal,NUpload} from 'naive-ui'
import {change_info, show_info} from "@/api/user";
import {ElMessage} from "element-plus";
import {login} from "@/api/login";

const info = reactive({
  user_info: {},
  new_info: {}
})
const showIdModal = ref(false)
const showAddressModal = ref(false)
const showCardModal = ref(false)
const showPasswordModal = ref(false)

const pw = reactive({
  oldPw: '',
  newPw: '',
  confirmPw: '',
})
const pwRef = ref(null)

const validatePass = (rule, value, callback) => {
  if (value.toString().length < 6) {
    callback(new Error('请设置至少6位的密码'))
  } else {
    if (pw.confirmPw !== '') {
      console.log(pwRef.value)
      if (!pwRef.value) return
      pwRef.value.validateField('confirmPw', () => null)
    }
    callback()
  }
}
const validatePass2 = (rule, value, callback) => {
  if (value === '') {
    callback(new Error('请再次输入密码'))
  } else if (value !== pw.newPw) {
    callback(new Error('两次输入密码不一致'))
  } else {
    callback()
  }
}

const rules = ref({
  oldPw: [
    {
      required: true,
      message: '请输入旧密码',
      trigger: 'blur'
    }
  ],
  newPw: [
    {
      validator: validatePass,
      trigger: 'change'
    },
    {
      required: true,
      validator: validatePass,
      trigger: 'blur'
    }
  ],
  confirmPw: [
    {
      validator: validatePass2,
      trigger: 'change'
    },
    {
      required: true,
      validator: validatePass2,
      trigger: 'blur'
    }
  ]
})

const renewInfo = () => {
  show_info().then(res => {
    let content = res.data
    console.log(content)
    if (content.code === "200") {
      info.user_info = content.user_info
      info.new_info = content.user_info
    }
  })
}

const changeName = () => {
  change_info({
    type: "name",
    info: info.new_info.name
  }).then(res => {
    let content = res.data
    console.log(content)
    ElMessage({message: content.message, type: content.hint})
  })
  showIdModal.value = false
}

const changeAddr = () => {
  change_info({
    type: "address",
    info: info.new_info.address
  }).then(res => {
    let content = res.data
    console.log(content)
    ElMessage({message: content.message, type: content.hint})
  })
  showAddressModal.value = false
}

const changeCard = () => {
  change_info({
    type: "card_num",
    info: info.new_info.card_num
  }).then(res => {
    let content = res.data
    console.log(content)
    ElMessage({message: content.message, type: content.hint})
  })
  showCardModal.value = false
}

const changePw = () => {
  // if (pw.oldPw !== info.user_info.password) {
  //   ElMessage({message: "旧密码错误", type: "error"})
  //   return
  // }
  if (pw.newPw !== pw.confirmPw) {
    ElMessage({message: "未确认新密码", type: "error"})
    return
  }
  change_info({
    type: "password",
    info: pw.oldPw,
    info2: pw.newPw
  }).then(res => {
    let content = res.data
    console.log(content)
    ElMessage({message: content.message, type: content.hint})
    login({
      name: info.new_info.name,
      password: pw.newPw
    }).then(res => {
      let content = res.data
      console.log(content)
    })
  })
  showPasswordModal.value = false
}

onMounted(() => {
  show_info().then(res => {
    let content = res.data
    console.log(content)
    if (content.code === "200") {
      info.user_info = content.user_info
      info.new_info = content.user_info
    } else {
      ElMessage({message: content.message, type: "error"})
    }
  })
})

</script>