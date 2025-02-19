UPDATE public.subscriptions_details
SET ru_description = 
    CASE 
        WHEN subscription_name = 'monthly_bomz' THEN '{"buy_info": "🍿Silver – идеальный старт", "price_hint": "🎬 Вместо билета в кино – попробуй всю мощь Dolly AI и ощути, как легко создавать шедевры! А если захочешь большего, вернешься сюда еще раз👉👈"}'::jsonb
        WHEN subscription_name = 'monthly_small' THEN '{"buy_info": "🏆Gold – выбор тех, кто хочет больше", "price_hint": "☕ Вместо трёх чашек кофе – контент, который собирает лайки!"}'::jsonb
        WHEN subscription_name = 'monthly_middle' THEN '{"buy_info": "💎 Platinum – продвинутый уровень", "price_hint": "🚕 Вместо одной поездки на такси – целый месяц крутых снимков!"}'::jsonb
        WHEN subscription_name = 'monthly_large' THEN '{"buy_info": "👑 Diamond", "price_hint": "💐 Вместо букета цветов – фотосессия, которая покоряет!"}'::jsonb
        ELSE '{}'::jsonb
    end
WHERE subscription_name IS NOT NULL