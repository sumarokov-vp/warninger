CREATE OR REPLACE FUNCTION public.create_test_objects()
 RETURNS void
 LANGUAGE plpgsql
AS $function$
DECLARE
  created_user_id numeric;
  created_warning_id numeric;
  created_recipient_id numeric;
  test_meassage_text text;
BEGIN
  test_meassage_text = 'Test message';
  INSERT INTO users
  (username, chat_id)
  VALUES
  ('Test user', 65310)
  ON CONFLICT ("chat_id") DO UPDATE
  SET
      username = EXCLUDED.username
  RETURNING id INTO created_user_id;


  SELECT id INTO created_warning_id FROM warnings
  WHERE message = test_meassage_text AND user_id = created_user_id;
  IF created_warning_id IS NULL THEN
    INSERT INTO warnings
    (message, user_id)
    VALUES
    (test_meassage_text, created_user_id)
    RETURNING id INTO created_warning_id;
  END IF;

  SELECT id INTO created_recipient_id FROM recipients
  WHERE warning_id = created_warning_id;
  IF created_recipient_id IS NULL THEN
    INSERT INTO recipients
    (name, chat_id, warning_id)
    VALUES ('Vova', 65310, created_warning_id);
  END IF;

  INSERT INTO settings
  (name, value)
  VALUES
  ('listen_port', '5052'),
  ('bot_token', '<BOT_TOKEN>'),
  ('reporter_sleep_time_sec', '100')
  ON CONFLICT ("name") DO UPDATE SET
  name = EXCLUDED.name;

  INSERT INTO warning_status
  (name, success)
  VALUES
  ('Active success', true),
  ('Active warning', false),
  ('Deactivated', false)
  ON CONFLICT ("name") DO UPDATE SET
  name = EXCLUDED.name,
  success = EXCLUDED.success;

END;
$function$;
