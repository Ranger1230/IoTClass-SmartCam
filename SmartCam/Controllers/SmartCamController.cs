using System.IO;
using System.Web;
using System.Web.Mvc;
using System.Net.Mail;

namespace SmartCam.Controllers
{
    public class SmartCamController : Controller
    {
        private static byte[] currentImage = new byte[0];

        [HttpPost]
        public string PostImage(HttpPostedFileBase file)
        {
            Stream fileStream = file.InputStream;
            using (MemoryStream ms = new MemoryStream())
            {
                fileStream.CopyTo(ms);
                currentImage = ms.GetBuffer();
            }
            return "Success";
        }

        [HttpGet]
        public FileResult GetPicture()
        {
            return new FileStreamResult(new MemoryStream(currentImage), "image/jpeg");
        }

        [HttpGet]
        public ActionResult ShowFeed()
        {
            return View();
        }

        [HttpGet]
        public string SendNotification()
        {
            var fromAddress = new MailAddress(from, "From Name");
            var toAddress = new MailAddress(to, "To Name");
            const string fromPassword = ;
            const string subject = "SmartCam";
            const string body = "Motion Detected!";

            using (SmtpClient smtp = new SmtpClient
            {
                Host = "smtp.gmail.com",
                Port = 587,
                EnableSsl = true,
                DeliveryMethod = SmtpDeliveryMethod.Network,
                UseDefaultCredentials = false,
                Credentials = new System.Net.NetworkCredential(fromAddress.Address, fromPassword)
            })
            {
                using (var message = new MailMessage(fromAddress, toAddress)
                {
                    Subject = subject,
                    Body = body
                })
                {
                    smtp.Send(message);
                }
            }
            return "Success";
        }
    }
}
