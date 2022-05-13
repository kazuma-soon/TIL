import express from 'express'
import messageController from './controllers/message'

const app: express.Express = express()

// 追加 サーバの強化追加
app.use(express.json())
app.use(express.urlencoded({ extended: true }))
// 追加終了

// 追加 処理の外だし
app.use("/messages", messageController)
// 追加終了

// 3000番ポートでAPIサーバ起動
app.listen(3000, () => {
    console.log('ポート3000番で起動しましたよ。')
})