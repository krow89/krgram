from krgram.tl.api.types.contacts import MyLink, ForeignLink, Link
from krgram.tl.core_types.native import TL_long, TL_string, TL_bytes, TL_double
from krgram.tl.types import *


class error(TLConstructor):
	ID = 0xc4b9f9bb

	def get_structure(self):
		return ("code", TL_int()), ("text", TL_string()),


class null(TLConstructor):
	ID = 0x56730bcc


class inputPeerEmpty(TLConstructor):
	ID = 0x7f3b18ea


class inputPeerSelf(TLConstructor):
	ID = 0x7da07ec9


class inputPeerContact(TLConstructor):
	ID = 0x1023dbe8

	def get_structure(self):
		return ("user_id", TL_int()),


class inputPeerForeign(TLConstructor):
	ID = 0x9b447325

	def get_structure(self):
		return ("user_id", TL_int()), ("access_hash", TL_long()),


class inputPeerChat(TLConstructor):
	ID = 0x179be863

	def get_structure(self):
		return ("chat_id", TL_int()),


class inputUserEmpty(TLConstructor):
	ID = 0xb98886cf


class inputUserSelf(TLConstructor):
	ID = 0xf7c1b13f


class inputUserContact(TLConstructor):
	ID = 0x86e94f65

	def get_structure(self):
		return ("user_id", TL_int()),


class inputUserForeign(TLConstructor):
	ID = 0x655e74ff

	def get_structure(self):
		return ("user_id", TL_int()), ("access_hash", TL_long()),


class inputPhoneContact(TLConstructor):
	ID = 0xf392b7f4

	def get_structure(self):
		return ("client_id", TL_long()), ("phone", TL_string()), ("first_name", TL_string()), (
			"last_name", TL_string()),


class inputFile(TLConstructor):
	ID = 0xf52ff27f

	def get_structure(self):
		return ("id", TL_long()), ("parts", TL_int()), ("name", TL_string()), ("md5_checksum", TL_string()),


class inputFileBig(TLConstructor):
	ID = 0xfa4f0bb5

	def get_structure(self):
		return ("id", TL_long()), ("parts", TL_int()), ("name", TL_string()),


class inputMediaEmpty(TLConstructor):
	ID = 0x9664f57f


class inputMediaUploadedPhoto(TLConstructor):
	ID = 0x2dc53a7d

	def get_structure(self):
		return ("file", InputFile()),


class inputMediaPhoto(TLConstructor):
	ID = 0x8f2ab2ec

	def get_structure(self):
		return ("id", InputPhoto()),


class inputMediaGeoPoint(TLConstructor):
	ID = 0xf9c44144

	def get_structure(self):
		return ("geo_point", InputGeoPoint()),


class inputMediaContact(TLConstructor):
	ID = 0xa6e45987

	def get_structure(self):
		return ("phone_number", TL_string()), ("first_name", TL_string()), ("last_name", TL_string()),


class inputMediaUploadedVideo(TLConstructor):
	ID = 0x133ad6f6

	def get_structure(self):
		return ("file", InputFile()), ("duration", TL_int()), ("w", TL_int()), ("h", TL_int()), (
			"mime_type", TL_string()),


class inputMediaUploadedThumbVideo(TLConstructor):
	ID = 0x9912dabf

	def get_structure(self):
		return ("file", InputFile()), ("thumb", InputFile()), ("duration", TL_int()), ("w", TL_int()), (
			"h", TL_int()), ("mime_type", TL_string()),


class inputMediaVideo(TLConstructor):
	ID = 0x7f023ae6

	def get_structure(self):
		return ("id", InputVideo()),


class inputMediaUploadedAudio(TLConstructor):
	ID = 0x4e498cab

	def get_structure(self):
		return ("file", InputFile()), ("duration", TL_int()), ("mime_type", TL_string()),


class inputMediaAudio(TLConstructor):
	ID = 0x89938781

	def get_structure(self):
		return ("id", InputAudio()),


class inputMediaUploadedDocument(TLConstructor):
	ID = 0x34e794bd

	def get_structure(self):
		return ("file", InputFile()), ("file_name", TL_string()), ("mime_type", TL_string()),


class inputMediaUploadedThumbDocument(TLConstructor):
	ID = 0x3e46de5d

	def get_structure(self):
		return ("file", InputFile()), ("thumb", InputFile()), ("file_name", TL_string()), ("mime_type", TL_string()),


class inputMediaDocument(TLConstructor):
	ID = 0xd184e841

	def get_structure(self):
		return ("id", InputDocument()),


class inputChatPhotoEmpty(TLConstructor):
	ID = 0x1ca48f57


class inputChatUploadedPhoto(TLConstructor):
	ID = 0x94254732

	def get_structure(self):
		return ("file", InputFile()), ("crop", InputPhotoCrop()),


class inputChatPhoto(TLConstructor):
	ID = 0xb2e1bf08

	def get_structure(self):
		return ("id", InputPhoto()), ("crop", InputPhotoCrop()),


class inputGeoPointEmpty(TLConstructor):
	ID = 0xe4c123d6


class inputGeoPoint(TLConstructor):
	ID = 0xf3b7acc9

	def get_structure(self):
		return ("lat", TL_double()), ("long", TL_double()),


class inputPhotoEmpty(TLConstructor):
	ID = 0x1cd7bf0d


class inputPhoto(TLConstructor):
	ID = 0xfb95c6c4

	def get_structure(self):
		return ("id", TL_long()), ("access_hash", TL_long()),


class inputVideoEmpty(TLConstructor):
	ID = 0x5508ec75


class inputVideo(TLConstructor):
	ID = 0xee579652

	def get_structure(self):
		return ("id", TL_long()), ("access_hash", TL_long()),


class inputFileLocation(TLConstructor):
	ID = 0x14637196

	def get_structure(self):
		return ("volume_id", TL_long()), ("local_id", TL_int()), ("secret", TL_long()),


class inputVideoFileLocation(TLConstructor):
	ID = 0x3d0364ec

	def get_structure(self):
		return ("id", TL_long()), ("access_hash", TL_long()),


class inputEncryptedFileLocation(TLConstructor):
	ID = 0xf5235d55

	def get_structure(self):
		return ("id", TL_long()), ("access_hash", TL_long()),


class inputAudioFileLocation(TLConstructor):
	ID = 0x74dc404d

	def get_structure(self):
		return ("id", TL_long()), ("access_hash", TL_long()),


class inputDocumentFileLocation(TLConstructor):
	ID = 0x4e45abe9

	def get_structure(self):
		return ("id", TL_long()), ("access_hash", TL_long()),


class inputPhotoCropAuto(TLConstructor):
	ID = 0xade6b004


class inputPhotoCrop(TLConstructor):
	ID = 0xd9915325

	def get_structure(self):
		return ("crop_left", TL_double()), ("crop_top", TL_double()), ("crop_width", TL_double()),


class inputAppEvent(TLConstructor):
	ID = 0x770656a8

	def get_structure(self):
		return ("time", TL_double()), ("type", TL_string()), ("peer", TL_long()), ("data", TL_string()),


class peerUser(TLConstructor):
	ID = 0x9db1bc6d

	def get_structure(self):
		return ("user_id", TL_int()),


class peerChat(TLConstructor):
	ID = 0xbad0e5bb

	def get_structure(self):
		return ("chat_id", TL_int()),


class fileLocationUnavailable(TLConstructor):
	ID = 0x7c596b46

	def get_structure(self):
		return ("volume_id", TL_long()), ("local_id", TL_int()), ("secret", TL_long()),


class fileLocation(TLConstructor):
	ID = 0x53d69076

	def get_structure(self):
		return ("dc_id", TL_int()), ("volume_id", TL_long()), ("local_id", TL_int()), ("secret", TL_long()),


class userEmpty(TLConstructor):
	ID = 0x200250ba

	def get_structure(self):
		return ("id", TL_int()),


class userSelf(TLConstructor):
	ID = 0x7007b451

	def get_structure(self):
		return ("id", TL_int()), ("first_name", TL_string()), ("last_name", TL_string()), ("username", TL_string()), (
			"phone", TL_string()), ("photo", UserProfilePhoto()), ("status", UserStatus()), ("inactive", Bool()),


class userContact(TLConstructor):
	ID = 0xcab35e18

	def get_structure(self):
		return ("id", TL_int()), ("first_name", TL_string()), ("last_name", TL_string()), ("username", TL_string()), (
			"access_hash", TL_long()), ("phone", TL_string()), ("photo", UserProfilePhoto()), ("status", UserStatus()),


class userRequest(TLConstructor):
	ID = 0xd9ccc4ef

	def get_structure(self):
		return ("id", TL_int()), ("first_name", TL_string()), ("last_name", TL_string()), ("username", TL_string()), (
			"access_hash", TL_long()), ("phone", TL_string()), ("photo", UserProfilePhoto()), ("status", UserStatus()),


class userForeign(TLConstructor):
	ID = 0x75cf7a8

	def get_structure(self):
		return ("id", TL_int()), ("first_name", TL_string()), ("last_name", TL_string()), ("username", TL_string()), (
			"access_hash", TL_long()), ("photo", UserProfilePhoto()), ("status", UserStatus()),


class userDeleted(TLConstructor):
	ID = 0xd6016d7a

	def get_structure(self):
		return ("id", TL_int()), ("first_name", TL_string()), ("last_name", TL_string()), ("username", TL_string()),


class userProfilePhotoEmpty(TLConstructor):
	ID = 0x4f11bae1


class userProfilePhoto(TLConstructor):
	ID = 0xd559d8c8

	def get_structure(self):
		return ("photo_id", TL_long()), ("photo_small", FileLocation()), ("photo_big", FileLocation()),


class userStatusEmpty(TLConstructor):
	ID = 0x9d05049


class userStatusOnline(TLConstructor):
	ID = 0xedb93949

	def get_structure(self):
		return ("expires", TL_int()),


class userStatusOffline(TLConstructor):
	ID = 0x8c703f

	def get_structure(self):
		return ("was_online", TL_int()),


class chatEmpty(TLConstructor):
	ID = 0x9ba2d800

	def get_structure(self):
		return ("id", TL_int()),


class chat(TLConstructor):
	ID = 0x6e9c9bc7

	def get_structure(self):
		return ("id", TL_int()), ("title", TL_string()), ("photo", ChatPhoto()), ("participants_count", TL_int()), (
			"date", TL_int()), ("left", Bool()), ("version", TL_int()),


class chatForbidden(TLConstructor):
	ID = 0xfb0ccc41

	def get_structure(self):
		return ("id", TL_int()), ("title", TL_string()), ("date", TL_int()),


class chatFull(TLConstructor):
	ID = 0x630e61be

	def get_structure(self):
		return ("id", TL_int()), ("participants", ChatParticipants()), ("chat_photo", Photo()), (
			"notify_settings", PeerNotifySettings()),


class chatParticipant(TLConstructor):
	ID = 0xc8d7493e

	def get_structure(self):
		return ("user_id", TL_int()), ("inviter_id", TL_int()), ("date", TL_int()),


class chatParticipantsForbidden(TLConstructor):
	ID = 0xfd2bb8a

	def get_structure(self):
		return ("chat_id", TL_int()),


class chatParticipants(TLConstructor):
	ID = 0x7841b415

	def get_structure(self):
		return ("chat_id", TL_int()), ("admin_id", TL_int()), ("participants", Vector()), ("version", TL_int()),


class chatPhotoEmpty(TLConstructor):
	ID = 0x37c1011c


class chatPhoto(TLConstructor):
	ID = 0x6153276a

	def get_structure(self):
		return ("photo_small", FileLocation()), ("photo_big", FileLocation()),


class messageEmpty(TLConstructor):
	ID = 0x83e5de54

	def get_structure(self):
		return ("id", TL_int()),


class message(TLConstructor):
	ID = 0x567699b3

	def get_structure(self):
		return ("flags", TL_int()), ("id", TL_int()), ("from_id", TL_int()), ("to_id", Peer()), ("date", TL_int()), (
			"message", TL_string()), ("media", MessageMedia()),


class messageForwarded(TLConstructor):
	ID = 0xa367e716

	def get_structure(self):
		return ("flags", TL_int()), ("id", TL_int()), ("fwd_from_id", TL_int()), ("fwd_date", TL_int()), \
			   ("from_id", TL_int()), ("to_id", Peer()), ("date", TL_int()), ("message", TL_string()), \
			   ("media", MessageMedia()),


class messageService(TLConstructor):
	ID = 0x1d86f70e

	def get_structure(self):
		return ("flags", TL_int()), ("id", TL_int()), ("from_id", TL_int()), ("to_id", Peer()), ("date", TL_int()), (
			"action", MessageAction()),


class messageMediaEmpty(TLConstructor):
	ID = 0x3ded6320


class messageMediaPhoto(TLConstructor):
	ID = 0xc8c45a2a

	def get_structure(self):
		return ("photo", Photo()),


class messageMediaVideo(TLConstructor):
	ID = 0xa2d24290

	def get_structure(self):
		return ("video", Video()),


class messageMediaGeo(TLConstructor):
	ID = 0x56e0d474

	def get_structure(self):
		return ("geo", GeoPoint()),


class messageMediaContact(TLConstructor):
	ID = 0x5e7d2f39

	def get_structure(self):
		return ("phone_number", TL_string()), ("first_name", TL_string()), ("last_name", TL_string()), (
			"user_id", TL_int()),


class messageMediaDocument(TLConstructor):
	ID = 0x2fda2204

	def get_structure(self):
		return ("document", Document()),


class messageMediaAudio(TLConstructor):
	ID = 0xc6b68300

	def get_structure(self):
		return ("audio", Audio()),


class messageActionEmpty(TLConstructor):
	ID = 0xb6aef7b0


class messageActionChatCreate(TLConstructor):
	ID = 0xa6638b9a

	def get_structure(self):
		return ("title", TL_string()), ("users", Vector()),


class messageActionChatEditTitle(TLConstructor):
	ID = 0xb5a1ce5a

	def get_structure(self):
		return ("title", TL_string()),


class messageActionChatEditPhoto(TLConstructor):
	ID = 0x7fcb13a8

	def get_structure(self):
		return ("photo", Photo()),


class messageActionChatDeletePhoto(TLConstructor):
	ID = 0x95e3fbef


class messageActionChatAddUser(TLConstructor):
	ID = 0x5e3cfc4b

	def get_structure(self):
		return ("user_id", TL_int()),


class messageActionChatDeleteUser(TLConstructor):
	ID = 0xb2ae9b0c

	def get_structure(self):
		return ("user_id", TL_int()),


class dialog(TLConstructor):
	ID = 0xab3a99ac

	def get_structure(self):
		return ("peer", Peer()), ("top_message", TL_int()), ("unread_count", TL_int()), (
			"notify_settings", PeerNotifySettings()),


class photoEmpty(TLConstructor):
	ID = 0x2331b22d

	def get_structure(self):
		return ("id", TL_long()),


class photo(TLConstructor):
	ID = 0x22b56751

	def get_structure(self):
		return ("id", TL_long()), ("access_hash", TL_long()), ("user_id", TL_int()), ("date", TL_int()), (
			"caption", TL_string()), ("geo", GeoPoint()), ("sizes", Vector()),


class photoSizeEmpty(TLConstructor):
	ID = 0xe17e23c

	def get_structure(self):
		return ("type", TL_string()),


class photoSize(TLConstructor):
	ID = 0x77bfb61b

	def get_structure(self):
		return ("type", TL_string()), ("location", FileLocation()), ("w", TL_int()), ("h", TL_int()), (
			"size", TL_int()),


class photoCachedSize(TLConstructor):
	ID = 0xe9a734fa

	def get_structure(self):
		return ("type", TL_string()), ("location", FileLocation()), ("w", TL_int()), ("h", TL_int()), (
			"bytes", TL_bytes()),


class videoEmpty(TLConstructor):
	ID = 0xc10658a8

	def get_structure(self):
		return ("id", TL_long()),


class video(TLConstructor):
	ID = 0x388fa391

	def get_structure(self):
		return ("id", TL_long()), ("access_hash", TL_long()), ("user_id", TL_int()), \
			   ("date", TL_int()), ("caption", TL_string()), ("duration", TL_int()), \
			   ("mime_type", TL_string()), ("size", TL_int()), ("thumb", PhotoSize()), \
			   ("dc_id", TL_int()), ("w", TL_int()), ("h", TL_int()),


class geoPointEmpty(TLConstructor):
	ID = 0x1117dd5f


class geoPoint(TLConstructor):
	ID = 0x2049d70c

	def get_structure(self):
		return ("long", TL_double()), ("lat", TL_double()),


class inputNotifyPeer(TLConstructor):
	ID = 0xb8bc5b0c

	def get_structure(self):
		return ("peer", InputPeer()),


class inputNotifyUsers(TLConstructor):
	ID = 0x193b4417


class inputNotifyChats(TLConstructor):
	ID = 0x4a95e84e


class inputNotifyAll(TLConstructor):
	ID = 0xa429b886


class inputPeerNotifyEventsEmpty(TLConstructor):
	ID = 0xf03064d8


class inputPeerNotifyEventsAll(TLConstructor):
	ID = 0xe86a2c74


class inputPeerNotifySettings(TLConstructor):
	ID = 0x46a2ce98

	def get_structure(self):
		return ("mute_until", TL_int()), ("sound", TL_string()), ("show_previews", Bool()), ("events_mask", TL_int()),


class peerNotifyEventsEmpty(TLConstructor):
	ID = 0xadd53cb3


class peerNotifyEventsAll(TLConstructor):
	ID = 0x6d1ded88


class peerNotifySettingsEmpty(TLConstructor):
	ID = 0x70a68512


class peerNotifySettings(TLConstructor):
	ID = 0x8d5e11ee

	def get_structure(self):
		return ("mute_until", TL_int()), ("sound", TL_string()), ("show_previews", Bool()), ("events_mask", TL_int()),


'''class peerSettings(TLConstructor):
	ID = 0x818426cd

	def get_structure(self):
		return ("flags", #()), ("report_spam", flags.0?true()),


class PeerSettings(TLConstructedType):
	CONSTRUCTORS_CLASSES = peerSettings,


TLRegister.register(PeerSettings)
'''


class wallPaper(TLConstructor):
	ID = 0xccb03657

	def get_structure(self):
		return ("id", TL_int()), ("title", TL_string()), ("sizes", Vector()), ("color", TL_int()),


class wallPaperSolid(TLConstructor):
	ID = 0x63117f24

	def get_structure(self):
		return ("id", TL_int()), ("title", TL_string()), ("bg_color", TL_int()), ("color", TL_int()),


class inputReportReasonSpam(TLConstructor):
	ID = 0x58dbcab8


class inputReportReasonViolence(TLConstructor):
	ID = 0x1e22c78d


class inputReportReasonPornography(TLConstructor):
	ID = 0x2e59d922


class inputReportReasonOther(TLConstructor):
	ID = 0xe1746d0a

	def get_structure(self):
		return ("text", TL_string()),


class userFull(TLConstructor):
	ID = 0x771095da

	def get_structure(self):
		return ("user", User()), ("link", Link()), ("profile_photo", Photo()), \
			   ("notify_settings", PeerNotifySettings()), ("blocked", Bool()), \
			   ("real_first_name", TL_string()), ("real_last_name", TL_string()),


class contact(TLConstructor):
	ID = 0xf911c994

	def get_structure(self):
		return ("user_id", TL_int()), ("mutual", Bool()),


class importedContact(TLConstructor):
	ID = 0xd0028438

	def get_structure(self):
		return ("user_id", TL_int()), ("client_id", TL_long()),


class contactBlocked(TLConstructor):
	ID = 0x561bc879

	def get_structure(self):
		return ("user_id", TL_int()), ("date", TL_int()),


class contactStatus(TLConstructor):
	ID = 0xaa77b873

	def get_structure(self):
		return ("user_id", TL_int()), ("expires", TL_int()),


class inputMessagesFilterEmpty(TLConstructor):
	ID = 0x57e2f66c


class inputMessagesFilterPhotos(TLConstructor):
	ID = 0x9609a51c


class inputMessagesFilterVideo(TLConstructor):
	ID = 0x9fc00e65


class inputMessagesFilterPhotoVideo(TLConstructor):
	ID = 0x56e9f0e4


class inputMessagesFilterDocument(TLConstructor):
	ID = 0x9eddf188


class inputMessagesFilterAudio(TLConstructor):
	ID = 0xcfc87522


class inputMessagesFilterAudioDocuments(TLConstructor):
	ID = 0x5afbf764


class inputMessagesFilterUrl(TLConstructor):
	ID = 0x7ef0dd87


class inputMessagesFilterGif(TLConstructor):
	ID = 0xffc86587


class updateNewMessage(TLConstructor):
	ID = 0x13abdb3

	def get_structure(self):
		return ("message", Message()), ("pts", TL_int()),


class updateMessageID(TLConstructor):
	ID = 0x4e90bfd6

	def get_structure(self):
		return ("id", TL_int()), ("random_id", TL_long()),


class updateReadMessages(TLConstructor):
	ID = 0xc6649e31

	def get_structure(self):
		return ("messages", Vector()), ("pts", TL_int()),


class updateDeleteMessages(TLConstructor):
	ID = 0xa92bfe26

	def get_structure(self):
		return ("messages", Vector()), ("pts", TL_int()),


class updateUserTyping(TLConstructor):
	ID = 0x5c486927

	def get_structure(self):
		return ("user_id", TL_int()), ("action", SendMessageAction()),


class updateChatUserTyping(TLConstructor):
	ID = 0x9a65ea1f

	def get_structure(self):
		return ("chat_id", TL_int()), ("user_id", TL_int()), ("action", SendMessageAction()),


class updateChatParticipants(TLConstructor):
	ID = 0x7761198

	def get_structure(self):
		return ("participants", ChatParticipants()),


class updateUserStatus(TLConstructor):
	ID = 0x1bfbd823

	def get_structure(self):
		return ("user_id", TL_int()), ("status", UserStatus()),


class updateUserName(TLConstructor):
	ID = 0xa7332b73

	def get_structure(self):
		return ("user_id", TL_int()), ("first_name", TL_string()), ("last_name", TL_string()), (
			"username", TL_string()),


class updateUserPhoto(TLConstructor):
	ID = 0x95313b0c

	def get_structure(self):
		return ("user_id", TL_int()), ("date", TL_int()), ("photo", UserProfilePhoto()), ("previous", Bool()),


class updateContactRegistered(TLConstructor):
	ID = 0x2575bbb9

	def get_structure(self):
		return ("user_id", TL_int()), ("date", TL_int()),


class updateContactLink(TLConstructor):
	ID = 0x51a48a9a

	def get_structure(self):
		return ("user_id", TL_int()), ("my_link", MyLink()), ("foreign_link", ForeignLink()),


class updateNewAuthorization(TLConstructor):
	ID = 0x8f06529a

	def get_structure(self):
		return ("auth_key_id", TL_long()), ("date", TL_int()), ("device", TL_string()), ("location", TL_string()),


class updateNewEncryptedMessage(TLConstructor):
	ID = 0x12bcbd9a

	def get_structure(self):
		return ("message", EncryptedMessage()), ("qts", TL_int()),


class updateEncryptedChatTyping(TLConstructor):
	ID = 0x1710f156

	def get_structure(self):
		return ("chat_id", TL_int()),


class updateEncryption(TLConstructor):
	ID = 0xb4a2e88d

	def get_structure(self):
		return ("chat", EncryptedChat()), ("date", TL_int()),


class updateEncryptedMessagesRead(TLConstructor):
	ID = 0x38fe25b7

	def get_structure(self):
		return ("chat_id", TL_int()), ("max_date", TL_int()), ("date", TL_int()),


class updateChatParticipantAdd(TLConstructor):
	ID = 0x3a0eeb22

	def get_structure(self):
		return ("chat_id", TL_int()), ("user_id", TL_int()), ("inviter_id", TL_int()), ("version", TL_int()),


class updateChatParticipantDelete(TLConstructor):
	ID = 0x6e5f8c22

	def get_structure(self):
		return ("chat_id", TL_int()), ("user_id", TL_int()), ("version", TL_int()),


class updateDcOptions(TLConstructor):
	ID = 0x8e5e9873

	def get_structure(self):
		return ("dc_options", Vector()),


class updateUserBlocked(TLConstructor):
	ID = 0x80ece81a

	def get_structure(self):
		return ("user_id", TL_int()), ("blocked", Bool()),


class updateNotifySettings(TLConstructor):
	ID = 0xbec268ef

	def get_structure(self):
		return ("peer", NotifyPeer()), ("notify_settings", PeerNotifySettings()),


class updateServiceNotification(TLConstructor):
	ID = 0x382dd3e4

	def get_structure(self):
		return ("type", TL_string()), ("message", TL_string()), ("media", MessageMedia()), ("popup", Bool()),


class updatesTooLong(TLConstructor):
	ID = 0xe317af7e


class updateShortMessage(TLConstructor):
	ID = 0xd3f45784

	def get_structure(self):
		return ("id", TL_int()), ("from_id", TL_int()), ("message", TL_string()), ("pts", TL_int()), (
			"date", TL_int()), ("seq", TL_int()),


class updateShortChatMessage(TLConstructor):
	ID = 0x2b2fbd4e

	def get_structure(self):
		return ("id", TL_int()), ("from_id", TL_int()), ("chat_id", TL_int()), ("message", TL_string()), (
			"pts", TL_int()), ("date", TL_int()), ("seq", TL_int()),


class updateShort(TLConstructor):
	ID = 0x78d4dec1

	def get_structure(self):
		return ("update", Update()), ("date", TL_int()),


class updatesCombined(TLConstructor):
	ID = 0x725b04c3

	def get_structure(self):
		return ("updates", Vector()), ("users", Vector()), ("chats", Vector()), ("date", TL_int()), (
			"seq_start", TL_int()), ("seq", TL_int()),


class updates(TLConstructor):
	ID = 0x74ae4240

	def get_structure(self):
		return ("updates", Vector()), ("users", Vector()), ("chats", Vector()), ("date", TL_int()), ("seq", TL_int()),


class dcOption(TLConstructor):
	ID = 0x2ec2a43c

	def get_structure(self):
		return ("id", TL_int()), ("hostname", TL_string()), ("ip_address", TL_string()), ("port", TL_int()),


class config(TLConstructor):
	ID = 0x2e54dd74

	def get_structure(self):
		return ("date", TL_int()), ("test_mode", Bool()), ("this_dc", TL_int()), ("dc_options", Vector()), (
			"chat_size_max", TL_int()), ("broadcast_size_max", TL_int()),


class nearestDc(TLConstructor):
	ID = 0x8e1a1775

	def get_structure(self):
		return ("country", TL_string()), ("this_dc", TL_int()), ("nearest_dc", TL_int()),


class encryptedChatEmpty(TLConstructor):
	ID = 0xab7ec0a0

	def get_structure(self):
		return ("id", TL_int()),


class encryptedChatWaiting(TLConstructor):
	ID = 0x3bf703dc

	def get_structure(self):
		return ("id", TL_int()), ("access_hash", TL_long()), ("date", TL_int()), ("admin_id", TL_int()), (
			"participant_id", TL_int()),


class encryptedChatRequested(TLConstructor):
	ID = 0xc878527e

	def get_structure(self):
		return ("id", TL_int()), ("access_hash", TL_long()), ("date", TL_int()), ("admin_id", TL_int()), (
			"participant_id", TL_int()), ("g_a", TL_bytes()),


class encryptedChat(TLConstructor):
	ID = 0xfa56ce36

	def get_structure(self):
		return ("id", TL_int()), ("access_hash", TL_long()), ("date", TL_int()), ("admin_id", TL_int()), (
			"participant_id", TL_int()), ("g_a_or_b", TL_bytes()), ("key_fingerprint", TL_long()),


class encryptedChatDiscarded(TLConstructor):
	ID = 0x13d6dd27

	def get_structure(self):
		return ("id", TL_int()),


class inputEncryptedChat(TLConstructor):
	ID = 0xf141b5e1

	def get_structure(self):
		return ("chat_id", TL_int()), ("access_hash", TL_long()),


class encryptedFileEmpty(TLConstructor):
	ID = 0xc21f497e


class encryptedFile(TLConstructor):
	ID = 0x4a70994c

	def get_structure(self):
		return ("id", TL_long()), ("access_hash", TL_long()), ("size", TL_int()), ("dc_id", TL_int()), (
			"key_fingerprint", TL_int()),


class inputEncryptedFileEmpty(TLConstructor):
	ID = 0x1837c364


class inputEncryptedFileUploaded(TLConstructor):
	ID = 0x64bd0306

	def get_structure(self):
		return ("id", TL_long()), ("parts", TL_int()), ("md5_checksum", TL_string()), ("key_fingerprint", TL_int()),


class inputEncryptedFile(TLConstructor):
	ID = 0x5a17b5e5

	def get_structure(self):
		return ("id", TL_long()), ("access_hash", TL_long()),


class inputEncryptedFileBigUploaded(TLConstructor):
	ID = 0x2dc173c8

	def get_structure(self):
		return ("id", TL_long()), ("parts", TL_int()), ("key_fingerprint", TL_int()),


class encryptedMessage(TLConstructor):
	ID = 0xed18c118

	def get_structure(self):
		return ("random_id", TL_long()), ("chat_id", TL_int()), ("date", TL_int()), ("bytes", TL_bytes()), (
			"file", EncryptedFile()),


class encryptedMessageService(TLConstructor):
	ID = 0x23734b06

	def get_structure(self):
		return ("random_id", TL_long()), ("chat_id", TL_int()), ("date", TL_int()), ("bytes", TL_bytes()),


class inputAudioEmpty(TLConstructor):
	ID = 0xd95adc84


class inputAudio(TLConstructor):
	ID = 0x77d440ff

	def get_structure(self):
		return ("id", TL_long()), ("access_hash", TL_long()),


class inputDocumentEmpty(TLConstructor):
	ID = 0x72f0eaae


class inputDocument(TLConstructor):
	ID = 0x18798952

	def get_structure(self):
		return ("id", TL_long()), ("access_hash", TL_long()),


class audioEmpty(TLConstructor):
	ID = 0x586988d8

	def get_structure(self):
		return ("id", TL_long()),


class audio(TLConstructor):
	ID = 0xc7ac6496

	def get_structure(self):
		return ("id", TL_long()), ("access_hash", TL_long()), ("user_id", TL_int()), ("date", TL_int()), (
			"duration", TL_int()), ("mime_type", TL_string()), ("size", TL_int()), ("dc_id", TL_int()),


class documentEmpty(TLConstructor):
	ID = 0x36f8c871

	def get_structure(self):
		return ("id", TL_long()),


class document(TLConstructor):
	ID = 0x9efc6326

	def get_structure(self):
		return ("id", TL_long()), ("access_hash", TL_long()), ("user_id", TL_int()), \
			   ("date", TL_int()), ("file_name", TL_string()), ("mime_type", TL_string()), \
			   ("size", TL_int()), ("thumb", PhotoSize()), ("dc_id", TL_int()),


class notifyPeer(TLConstructor):
	ID = 0x9fd40bd8

	def get_structure(self):
		return ("peer", Peer()),


class notifyUsers(TLConstructor):
	ID = 0xb4c83b4c


class notifyChats(TLConstructor):
	ID = 0xc007cec3


class notifyAll(TLConstructor):
	ID = 0x74d07c60


class sendMessageTypingAction(TLConstructor):
	ID = 0x16bf744e


class sendMessageCancelAction(TLConstructor):
	ID = 0xfd5ec8f5


class sendMessageRecordVideoAction(TLConstructor):
	ID = 0xa187d66f


class sendMessageUploadVideoAction(TLConstructor):
	ID = 0x92042ff7


class sendMessageRecordAudioAction(TLConstructor):
	ID = 0xd52f73f7


class sendMessageUploadAudioAction(TLConstructor):
	ID = 0xe6ac8a6f


class sendMessageUploadPhotoAction(TLConstructor):
	ID = 0x990a3c1a


class sendMessageUploadDocumentAction(TLConstructor):
	ID = 0x8faee98e


class sendMessageGeoLocationAction(TLConstructor):
	ID = 0x176f8ba1


class sendMessageChooseContactAction(TLConstructor):
	ID = 0x628cbc6f


class contactFound(TLConstructor):
	ID = 0xea879f95

	def get_structure(self):
		return ("user_id", TL_int()),


class EncryptedMessage(TLConstructedType):
	CONSTRUCTORS_CLASSES = encryptedMessage, encryptedMessageService,


TLRegister.register(EncryptedMessage)


class InputNotifyPeer(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputNotifyPeer, inputNotifyUsers, inputNotifyChats, inputNotifyAll,


TLRegister.register(InputNotifyPeer)


class Document(TLConstructedType):
	CONSTRUCTORS_CLASSES = documentEmpty, document,


TLRegister.register(Document)


class EncryptedFile(TLConstructedType):
	CONSTRUCTORS_CLASSES = encryptedFileEmpty, encryptedFile,


TLRegister.register(EncryptedFile)


class Update(TLConstructedType):
	CONSTRUCTORS_CLASSES = updateNewMessage, updateMessageID, updateReadMessages, \
						   updateDeleteMessages, updateUserTyping, updateChatUserTyping, \
						   updateChatParticipants, updateUserStatus, updateUserName, \
						   updateUserPhoto, updateContactRegistered, updateContactLink, \
						   updateNewAuthorization, updateNewEncryptedMessage, updateEncryptedChatTyping, \
						   updateEncryption, updateEncryptedMessagesRead, updateChatParticipantAdd, \
						   updateChatParticipantDelete, updateDcOptions, updateUserBlocked, \
						   updateNotifySettings, updateServiceNotification,


TLRegister.register(Update)


class InputChatPhoto(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputChatPhotoEmpty, inputChatUploadedPhoto, inputChatPhoto,


TLRegister.register(InputChatPhoto)


class PeerNotifySettings(TLConstructedType):
	CONSTRUCTORS_CLASSES = peerNotifySettingsEmpty, peerNotifySettings,


TLRegister.register(PeerNotifySettings)


class Peer(TLConstructedType):
	CONSTRUCTORS_CLASSES = peerUser, peerChat,


TLRegister.register(Peer)


class InputAppEvent(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputAppEvent,


TLRegister.register(InputAppEvent)


class InputEncryptedFile(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputEncryptedFileEmpty, inputEncryptedFileUploaded, inputEncryptedFile, inputEncryptedFileBigUploaded,


TLRegister.register(InputEncryptedFile)


class InputPhoto(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputPhotoEmpty, inputPhoto,


TLRegister.register(InputPhoto)


class UserProfilePhoto(TLConstructedType):
	CONSTRUCTORS_CLASSES = userProfilePhotoEmpty, userProfilePhoto,


TLRegister.register(UserProfilePhoto)


class InputUser(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputUserEmpty, inputUserSelf, inputUserContact, inputUserForeign,


TLRegister.register(InputUser)


class DcOption(TLConstructedType):
	CONSTRUCTORS_CLASSES = dcOption,


TLRegister.register(DcOption)


class GeoPoint(TLConstructedType):
	CONSTRUCTORS_CLASSES = geoPointEmpty, geoPoint,


TLRegister.register(GeoPoint)


class WallPaper(TLConstructedType):
	CONSTRUCTORS_CLASSES = wallPaper, wallPaperSolid,


TLRegister.register(WallPaper)


class ChatFull(TLConstructedType):
	CONSTRUCTORS_CLASSES = chatFull,


TLRegister.register(ChatFull)


class InputGeoPoint(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputGeoPointEmpty, inputGeoPoint,


TLRegister.register(InputGeoPoint)


class InputPeerNotifyEvents(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputPeerNotifyEventsEmpty, inputPeerNotifyEventsAll,


TLRegister.register(InputPeerNotifyEvents)


class InputFile(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputFile, inputFileBig,


TLRegister.register(InputFile)


class InputPeerNotifySettings(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputPeerNotifySettings,


TLRegister.register(InputPeerNotifySettings)


class Contact(TLConstructedType):
	CONSTRUCTORS_CLASSES = contact,


TLRegister.register(Contact)


class PhotoSize(TLConstructedType):
	CONSTRUCTORS_CLASSES = photoSizeEmpty, photoSize, photoCachedSize,


TLRegister.register(PhotoSize)


class Photo(TLConstructedType):
	CONSTRUCTORS_CLASSES = photoEmpty, photo,


TLRegister.register(Photo)


class ReportReason(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputReportReasonSpam, inputReportReasonViolence, inputReportReasonPornography, inputReportReasonOther,


TLRegister.register(ReportReason)


class Message(TLConstructedType):
	CONSTRUCTORS_CLASSES = messageEmpty, message, messageForwarded, messageService,


TLRegister.register(Message)


class Null(TLConstructedType):
	CONSTRUCTORS_CLASSES = null,


TLRegister.register(Null)


class ChatPhoto(TLConstructedType):
	CONSTRUCTORS_CLASSES = chatPhotoEmpty, chatPhoto,


TLRegister.register(ChatPhoto)


class NearestDc(TLConstructedType):
	CONSTRUCTORS_CLASSES = nearestDc,


TLRegister.register(NearestDc)


class Config(TLConstructedType):
	CONSTRUCTORS_CLASSES = config,


TLRegister.register(Config)


class User(TLConstructedType):
	CONSTRUCTORS_CLASSES = userEmpty, userSelf, userContact, userRequest, userForeign, userDeleted,


TLRegister.register(User)


class InputVideo(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputVideoEmpty, inputVideo,


TLRegister.register(InputVideo)


class MessageAction(TLConstructedType):
	CONSTRUCTORS_CLASSES = messageActionEmpty, messageActionChatCreate, messageActionChatEditTitle, messageActionChatEditPhoto, messageActionChatDeletePhoto, messageActionChatAddUser, messageActionChatDeleteUser,


TLRegister.register(MessageAction)


class MessagesFilter(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputMessagesFilterEmpty, inputMessagesFilterPhotos, inputMessagesFilterVideo, inputMessagesFilterPhotoVideo, inputMessagesFilterDocument, inputMessagesFilterAudio, inputMessagesFilterAudioDocuments, inputMessagesFilterUrl, inputMessagesFilterGif,


TLRegister.register(MessagesFilter)


class InputFileLocation(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputFileLocation, inputVideoFileLocation, inputEncryptedFileLocation, \
						   inputAudioFileLocation, inputDocumentFileLocation,


TLRegister.register(InputFileLocation)


class UserStatus(TLConstructedType):
	CONSTRUCTORS_CLASSES = userStatusEmpty, userStatusOnline, userStatusOffline,


TLRegister.register(UserStatus)


class Dialog(TLConstructedType):
	CONSTRUCTORS_CLASSES = dialog,


TLRegister.register(Dialog)


class Error(TLConstructedType):
	CONSTRUCTORS_CLASSES = error,


TLRegister.register(Error)


class NotifyPeer(TLConstructedType):
	CONSTRUCTORS_CLASSES = notifyPeer, notifyUsers, notifyChats, notifyAll,


TLRegister.register(NotifyPeer)


class ContactStatus(TLConstructedType):
	CONSTRUCTORS_CLASSES = contactStatus,


TLRegister.register(ContactStatus)


class FileLocation(TLConstructedType):
	CONSTRUCTORS_CLASSES = fileLocationUnavailable, fileLocation,


TLRegister.register(FileLocation)


class ImportedContact(TLConstructedType):
	CONSTRUCTORS_CLASSES = importedContact,


TLRegister.register(ImportedContact)


class Video(TLConstructedType):
	CONSTRUCTORS_CLASSES = videoEmpty, video,


TLRegister.register(Video)


class InputDocument(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputDocumentEmpty, inputDocument,


TLRegister.register(InputDocument)


class InputMedia(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputMediaEmpty, inputMediaUploadedPhoto, inputMediaPhoto, \
						   inputMediaGeoPoint, inputMediaContact, inputMediaUploadedVideo, inputMediaUploadedThumbVideo, inputMediaVideo, inputMediaUploadedAudio, inputMediaAudio, inputMediaUploadedDocument, inputMediaUploadedThumbDocument, inputMediaDocument,


TLRegister.register(InputMedia)


class SendMessageAction(TLConstructedType):
	CONSTRUCTORS_CLASSES = sendMessageTypingAction, sendMessageCancelAction, sendMessageRecordVideoAction, \
						   sendMessageUploadVideoAction, sendMessageRecordAudioAction, \
						   sendMessageUploadAudioAction, sendMessageUploadPhotoAction, \
						   sendMessageUploadDocumentAction, sendMessageGeoLocationAction, \
						   sendMessageChooseContactAction,


TLRegister.register(SendMessageAction)


class EncryptedChat(TLConstructedType):
	CONSTRUCTORS_CLASSES = encryptedChatEmpty, encryptedChatWaiting, encryptedChatRequested, \
						   encryptedChat, encryptedChatDiscarded,


TLRegister.register(EncryptedChat)


class InputPeer(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputPeerEmpty, inputPeerSelf, inputPeerContact, inputPeerForeign, inputPeerChat,


TLRegister.register(InputPeer)


class ChatParticipants(TLConstructedType):
	CONSTRUCTORS_CLASSES = chatParticipantsForbidden, chatParticipants,


TLRegister.register(ChatParticipants)


class InputAudio(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputAudioEmpty, inputAudio,


TLRegister.register(InputAudio)


class UserFull(TLConstructedType):
	CONSTRUCTORS_CLASSES = userFull,


TLRegister.register(UserFull)


class ContactBlocked(TLConstructedType):
	CONSTRUCTORS_CLASSES = contactBlocked,


TLRegister.register(ContactBlocked)


class MessageMedia(TLConstructedType):
	CONSTRUCTORS_CLASSES = messageMediaEmpty, messageMediaPhoto, messageMediaVideo, messageMediaGeo, \
						   messageMediaContact, messageMediaDocument, messageMediaAudio,


TLRegister.register(MessageMedia)


class PeerNotifyEvents(TLConstructedType):
	CONSTRUCTORS_CLASSES = peerNotifyEventsEmpty, peerNotifyEventsAll,


TLRegister.register(PeerNotifyEvents)


class Chat(TLConstructedType):
	CONSTRUCTORS_CLASSES = chatEmpty, chat, chatForbidden,


TLRegister.register(Chat)


class ContactFound(TLConstructedType):
	CONSTRUCTORS_CLASSES = contactFound,


TLRegister.register(ContactFound)


class InputContact(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputPhoneContact,


TLRegister.register(InputContact)


class ChatParticipant(TLConstructedType):
	CONSTRUCTORS_CLASSES = chatParticipant,


TLRegister.register(ChatParticipant)


class Audio(TLConstructedType):
	CONSTRUCTORS_CLASSES = audioEmpty, audio,


TLRegister.register(Audio)


class Updates(TLConstructedType):
	CONSTRUCTORS_CLASSES = updatesTooLong, updateShortMessage, updateShortChatMessage, updateShort, updatesCombined, updates,


TLRegister.register(Updates)


class InputEncryptedChat(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputEncryptedChat,


TLRegister.register(InputEncryptedChat)


class InputPhotoCrop(TLConstructedType):
	CONSTRUCTORS_CLASSES = inputPhotoCropAuto, inputPhotoCrop,


TLRegister.register(InputPhotoCrop)
