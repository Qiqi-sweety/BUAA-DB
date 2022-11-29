<!-- storeRegisterCard2的子组件，负责获得商家营业执照
其包含子组件storeRegisterLeft2——负责获得商家商家注册的店铺地址，店铺介绍，店铺头像 -->

<!-- TODO:
提交按钮：根据后端返回值
1.“信息不完整”出现弹窗
2.“提交成功”发送一个信号给storeRegisterCard2，storeRegisterCard2再传信号给storeRegisterPage，然后storeRegisterPage会切换到storeRegisterCard3组件

登录账号按钮：跳转到storeRegisterPage

返回首页按钮：跳转到firstPage -->

<template>
    
    <el-row
    style = "margin-right:0px;
            width:100%;">
      <el-col :span="12" class = "storeRegisterFormCol">
        <el-form 
          :model="form"
          :rules="rules"
          class="storeRegisterLeft2" 
        >
          <el-form-item prop="address" class = "addressInputBoxItem">
            <el-input
              v-model="form.address"
              type="address"
              placeholder="店铺地址"
              size = "large"
            >
              <template #prefix>
                <el-icon class="el-input__icon"><location /></el-icon>
              </template>
            </el-input>
      
          </el-form-item>

          <el-form-item prop="info" class = "introInputBoxItem">
            <el-input
                v-model="form.info"
                :autosize="{ minRows: 3, maxRows: 4 }"
                type="textarea"
                maxlength="500"
                show-word-limit
                placeholder="店铺介绍"
            >
            
            </el-input>
          </el-form-item>


          <el-form-item 
          style = "margin-top :5%;
                  margin-left:15%;
                  width: 300px;">
            <el-row style = "width: 300px;">


              <el-col :span="8">
                <p style = "text-align: center;
                      font-size: 15px;
                      margin-left: 5%;
                      font-weight: bold;
                      color:#606266;">上传店铺头像</p>
              </el-col>


              <el-col :span="12">
<!--                todo-->
                <el-upload
                class="logo-uploader"
                :show-file-list="false"
                :limit="1"
                action="/api/image/update/"
                list-type="picture"
                :on-success="handleLogoSuccess">
<!--                :before-upload="beforeLogoUpload"-->

                  <el-image v-if="form.logo" :src="`/api${form.logo}`" class="avatar" :fit='contain'/>
                  <el-icon v-else><Plus /></el-icon>
                </el-upload>
              </el-col>


            </el-row>

          </el-form-item>

          
          <el-form-item
          style="width: 300px;
          margin-top:2%;
          margin-left: auto;
          margin-right: auto;">
      
            <el-button 
              color = "#fec01b" 
              round
              plain
              size = "large"
              style="width: 300px;
                margin-top:2%;
                margin-left: auto;
                margin-right: auto;"
              @click="storeRegister2"
            >
              提交申请
            </el-button>
      
          </el-form-item>

          
      
          <el-form-item style = "width: 300px;
                                margin-top: 10px;
                                margin-left: 22%;
                                padding: 0;
                                margin-bottom: 10px;"
          >
            
            <el-row style = " width : 350px">
            <el-col :span="12">  
                <el-link :underline="false" @click="to_storeLoginPage">
                登录账号
              </el-link>
              </el-col>
            <el-col :span="12">
              <el-link :underline="false" @click="to_firstPage">
                返回首页
              </el-link>
            </el-col>
          </el-row>
              
          </el-form-item>
        </el-form>
      </el-col>


      <el-col :span="12" class = "storeRegisterImageFormCol">
<!--        todo-->
        <el-upload
          class="avatar-uploader-license"
          :show-file-list="false"
          :limit="1"
          action="/api/image/update/"
          list-type="picture-card"
          :on-success="handleLicenseSuccess">
<!--            :before-upload="beforeAvatarUpload"-->

          <el-image v-if="form.license" :src="`/api${form.license}`" class="avatar"/>
          <el-icon v-else><Plus /></el-icon>

        </el-upload>

<!--        <el-dialog v-model="dialogVisible2">-->
<!--          <img w-full :src="form.license" alt="图片预览" />-->
<!--        </el-dialog>-->

        <p class = "uploadDetail">上传营业执照</p>


      </el-col>


    </el-row>
  
</template>

<script setup>
import {ref, reactive, toRefs} from "vue"
import {ElMessage} from "element-plus"
import { Delete, Download, Plus, ZoomIn } from '@element-plus/icons-vue'
import {store_register_2} from "@/api/register";
import {useRouter} from "vue-router";
const router = useRouter()

const props = defineProps({
  // name: {type: String, required: true},
  // pw: {type: String, required: true}
  name: String,
  pw: String
})

// const former_form = toRefs(props)

const form = reactive({
  name: props.name,
  password: props.pw,
  address: '',
  info: '',
  logo: '',
  license: ''
})

const dialogVisible1 = ref(false)
const dialogVisible2 = ref(false)
const disabled1 = ref(false)
const disabled2 = ref(false)

const handleLogoSuccess = (res) => {
  console.log(res)
  form.logo = res.url
}

const handleLicenseSuccess = (res) => {
  console.log(res)
  form.license = res.url
}

const handleRemove = (file) => {
  console.log(file)
}

const handleLicensePreview = (file) => {
  form.license = file.url
  dialogVisible2.value = true
}

const handleDownload = (file) => {
  console.log(file)
}

const rules = ref({
  address: [
    {
      required: true,
      message: '请输入店铺地址',
      trigger: 'blur'
    }
  ],
  info: [
    {
      required: true,
      message: '请输入店铺介绍',
      trigger: 'blur'
    }
  ]
})

const storeRegister2 = () => {
  console.log(form)
  store_register_2(form)
      .then(res => {
        let content = res.data
        console.log(content)
        ElMessage({message: content.message, type: content.hint})
        if (content.code === '200') {
          router.push('/storeRegisterPage/step3')
        }
      })
}

const to_storeLoginPage = () => {
  router.push('/storeLoginPage')
}

const to_firstPage = () => {
  router.push('/')
}
</script>



<style>
/* .storeRegisterRow {
  margin-right:0px;
  width:100%;
} */


.storeRegisterLeft2 {
  margin-left: 100px;
  margin-bottom: 50px;
}

.introInputBoxItem {
  width: 300px;
  margin: 10px auto;
  height: 70px;
}

.storeRegisterImageFormClass {
  margin: auto;
}


.avatar-uploader-license .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
  .avatar-uploader-license {
    margin-left:150px;
  }

  .storeRegisterRight2 {
    width: 400px;
    height: 350px;
    /*padding: 30px;*/
    border-radius: 20px;
    /* 整个表单el-form位于整个屏幕的位置 margin */  

  }
  .storeRegisterRightItem {
    margin-top: 0;
    margin-left: 20%;
    
  }

  .uploadDetail {
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    color:#606266;
  }

    .avatar-uploader-license .el-upload {
    border: 1px dashed;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: var(--el-transition-duration-fast);
  }
  
  .avatar-uploader-license .el-upload:hover {
    border-color: var(--el-color-primary);
  }
  
  .el-icon.license-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 250px;
    height: 300px;
    text-align: center;
  }


</style>