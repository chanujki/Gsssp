<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8" />
  <title>Facebook Service Center – Rakib Mahmud</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    body {
      margin: 0;
      padding: 0;
      background: #0b0b0b;
      font-family: "Segoe UI", sans-serif;
      color: #e8e8e8;
      display: flex;
      justify-content: center;
      padding: 25px;
    }

    .container {
      width: 100%;
      max-width: 450px;
      background: #111;
      padding: 28px 22px;
      border-radius: 20px;
      border: 1px solid #1e1e1e;
      box-shadow: 0 0 40px rgba(0, 0, 0, 0.55);
    }

    .profile {
      text-align: center;
      margin-bottom: 20px;
    }

    .profile img {
      width: 120px;
      height: 120px;
      border-radius: 50%;
      border: 3px solid #00ffbf;
      object-fit: cover;
      box-shadow: 0 0 25px rgba(0, 255, 191, 0.25);
    }

    h1 {
      margin-top: 12px;
      font-size: 22px;
      font-weight: 700;
      color: #ffffff;
    }

    .tagline {
      font-size: 14px;
      margin-bottom: 20px;
      color: #9affdd;
    }

    .section-title {
      margin-top: 20px;
      font-size: 13px;
      color: #bbbbbb;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }

    ul {
      padding-left: 0;
      list-style: none;
      margin-top: 10px;
    }

    li {
      background: #181818;
      border: 1px solid #222;
      padding: 10px 12px;
      border-radius: 10px;
      margin-bottom: 8px;
      font-size: 14px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .emoji {
      font-size: 18px;
    }

    .whatsapp-btn {
      display: block;
      margin-top: 25px;
      text-align: center;
      padding: 12px 0;
      background: #00a884;
      border-radius: 10px;
      font-size: 15px;
      font-weight: bold;
      color: #fff;
      text-decoration: none;
      box-shadow: 0 0 20px rgba(0, 168, 132, 0.4);
    }

    .footer {
      margin-top: 15px;
      font-size: 11px;
      color: #666;
      text-align: center;
    }

    /* 🔽 নিচেরগুলো নতুন – ফর্ম ডিজাইন 🔽 */
    .form-box {
      margin-top: 25px;
      background: #151515;
      border-radius: 14px;
      padding: 14px 12px;
      border: 1px solid #222;
    }

    .form-box h2 {
      font-size: 16px;
      margin: 0 0 8px 0;
      color: #ffffff;
    }

    .form-box p {
      font-size: 12px;
      margin: 0 0 12px 0;
      color: #999999;
    }

    .form-group {
      margin-bottom: 10px;
    }

    .form-label {
      font-size: 12px;
      margin-bottom: 4px;
      display: block;
      color: #bbbbbb;
    }

    textarea,
    input[type="text"] {
      width: 100%;
      background: #101010;
      border: 1px solid #272727;
      border-radius: 10px;
      padding: 9px 10px;
      font-size: 13px;
      color: #f1f1f1;
      resize: vertical;
      min-height: 70px;
      box-sizing: border-box;
      outline: none;
    }

    textarea:focus,
    input[type="text"]:focus {
      border-color: #00ffbf;
      box-shadow: 0 0 10px rgba(0, 255, 191, 0.2);
    }

    .submit-btn {
      width: 100%;
      margin-top: 6px;
      padding: 10px 0;
      background: linear-gradient(135deg, #00ffbf, #00a884);
      border-radius: 10px;
      border: none;
      font-size: 14px;
      font-weight: 600;
      color: #071710;
      cursor: pointer;
      box-shadow: 0 0 18px rgba(0, 255, 191, 0.4);
    }

    .submit-btn:disabled {
      opacity: 0.7;
      cursor: not-allowed;
      box-shadow: none;
    }

    .status-message {
      margin-top: 8px;
      font-size: 12px;
      text-align: center;
      min-height: 16px;
    }

    .status-success {
      color: #6bffb0;
    }

    .status-error {
      color: #ff6b6b;
    }
  </style>
</head>
<body>

  <div class="container">

    <div class="profile">
      <img src="https://i.imgur.com/pJ46xv0.png" alt="Profile Image">
      <h1>Facebook Service Center</h1>
      <p class="tagline">আপনার যেকোনো ফেসবুক সমস্যার ১০০% সমাধান — ইনশাআল্লাহ</p>
    </div>

    <div class="section-title">আমাদের সার্ভিস</div>
    <ul>
      <li><span class="emoji">🔐</span> হ্যাকড আইডি/পেজ রিকভার</li>
      <li><span class="emoji">🔓</span> লক / ডিজেবল / সাসপেন্ড আইডি ব্যাক</li>
      <li><span class="emoji">🆔</span> ফেসবুক আইডি রানিং ভেরিফাই</li>
      <li><span class="emoji">⚙️</span> নাম, DOB, ইমেইল ও নাম্বার আপডেট</li>
      <li><span class="emoji">📲</span> 2FA / কোড না আসা / লগইন সমস্যা</li>
      <li><span class="emoji">📂</span> কমিউনিটি ডিজেবল / রিস্টোর (Read More সহ)</li>
      <li><span class="emoji">🚨</span> হার্জেন্ট কেস ইনস্ট্যান্ট সাপোর্ট</li>
      <li><span class="emoji">💳</span> কাস্টম বিকাশ একাউন্ট ডিজেবল ফিক্স</li>
    </ul>

    <a class="whatsapp-btn" href="https://wa.me/8801771306867" target="_blank">
      WhatsApp: 01771306867
    </a>

    <!-- 🔽 নতুন ফর্ম সেকশন – এখানে মানুষ নিজের সমস্যা জমা দেবে -->
    <div class="form-box">
      <h2>আপনার সমস্যা এখানে জমা দিন</h2>
      <p>যত ডিটেইল্স পারেন লিখুন। আপনার লেখা অটোমেটিক আমাদের টেলিগ্রামে পৌঁছে যাবে।</p>

      <form id="problemForm">
        <div class="form-group">
          <label class="form-label" for="contactInfo">আপনার নাম / নম্বর / আইডি লিংক (ঐচ্ছিক)</label>
          <input
            type="text"
            id="contactInfo"
            name="contactInfo"
            placeholder="যেমন: নাম, মোবাইল, ফেসবুক লিংক ইত্যাদি">
        </div>

        <div class="form-group">
          <label class="form-label" for="problemText">সমস্যার বিস্তারিত*</label>
          <textarea
            id="problemText"
            name="problemText"
            placeholder="এখানে আপনার সমস্যার বিস্তারিত লিখুন..."></textarea>
        </div>

        <button type="submit" class="submit-btn">আবেদন সাবমিট করুন</button>
        <div id="statusMessage" class="status-message"></div>
      </form>
    </div>

    <p class="footer">Design by Rakib Mahmud</p>

  </div>

  <!-- 🔽 টেলিগ্রাম এপিআই এর জন্য জাভাস্ক্রিপ্ট -->
  <script>
    // 🔐 নিজের টেলিগ্রাম বটের তথ্য এখানে বসাবে
    const BOT_TOKEN = "YOUR_BOT_TOKEN_HERE";  // 👉 BotFather থেকে নেয়া টোকেন
    const CHAT_ID = "YOUR_CHAT_ID_HERE";      // 👉 তোমার টেলিগ্রাম আইডি / গ্রুপ আইডি

    const form = document.getElementById("problemForm");
    const statusMessage = document.getElementById("statusMessage");
    const submitBtn = form.querySelector(".submit-btn");

    form.addEventListener("submit", async function (e) {
      e.preventDefault();

      const contactInfo = document.getElementById("contactInfo").value.trim();
      const problemText = document.getElementById("problemText").value.trim();

      if (!problemText) {
        statusMessage.textContent = "সমস্যার বিস্তারিত লিখে তারপর সাবমিট করুন।";
        statusMessage.className = "status-message status-error";
        return;
      }

      // সাবমিট করার সময় বাটন লক করি
      submitBtn.disabled = true;
      submitBtn.textContent = "পাঠানো হচ্ছে...";
      statusMessage.textContent = "";
      statusMessage.className = "status-message";

      // টেলিগ্রামে যাবে এমন ফাইনাল মেসেজ
      let finalMessage = "🆕 নতুন ফেসবুক সমস্যা জমা পড়েছে:\n\n";
      if (contactInfo) {
        finalMessage += "👤 কন্টাক্ট: " + contactInfo + "\n\n";
      }
      finalMessage += "📌 সমস্যা:\n" + problemText;

      const url = `https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`;

      try {
        const res = await fetch(url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            chat_id: CHAT_ID,
            text: finalMessage
          })
        });

        if (res.ok) {
          statusMessage.textContent = "✅ আপনার আবেদন সফলভাবে জমা হয়েছে। শীঘ্রই যোগাযোগ করা হবে ইনশাআল্লাহ।";
          statusMessage.className = "status-message status-success";
          form.reset();
        } else {
          statusMessage.textContent = "❌ সাময়িক সমস্যা হয়েছে। পরে আবার চেষ্টা করুন।";
          statusMessage.className = "status-message status-error";
        }
      } catch (err) {
        statusMessage.textContent = "❌ ইন্টারনেট সমস্যা বা টেলিগ্রাম এপিআই এ সমস্যা হচ্ছে।";
        statusMessage.className = "status-message status-error";
      } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = "আবেদন সাবমিট করুন";
      }
    });
  </script>

</body>
</html>
